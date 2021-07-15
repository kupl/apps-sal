class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        # left
        for i in range(1, n):
            if arr[i] >= arr[i-1]:
                l += 1
            else:   break
        
        # if l == n-1:    return 0
        # right
        for i in reversed(list(range(1, n))):
            if arr[i] >= arr[i-1]:
                r -= 1
            else:   break
        
        # left find right
        res = min(n-l, r)
        for i in reversed(list(range(1, l+1))):
            j = self.bsearch(arr, arr[i], r, n-1)
            if arr[j] < arr[i]:
                res = min(res, j-i)
            else:
                res = min(res, j-i-1)
            
        # right find left
        # [1,2,3,10,4,2,3,5]
        for i in range(r, n):
            j = self.bsearch(arr, arr[i], 0, l)
            if arr[j] > arr[i]:
                res = min(res, i-j)
            else:
                res = min(res, i-j-1)
                
        return max(0, res)
    
    def bsearch(self, A, target, s, e):
        while s < e:
            m = s + (e-s)//2
            if A[m] < target:
                s = m+1
            else:
                e = m
        return e
        

