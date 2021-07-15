class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if not arr: return 0
        arr = [-10000000] + arr
        i = 0
        for j in range(i+1, len(arr)):
            if arr[j] >= arr[i]:
                i += 1
            else:
                break
        
        firsti = i
        
        j = len(arr)-1
        for i in range(j-1, -1, -1):
            if arr[j] >= arr[i]:
                j -=1
            else:
                break
        lastj = j
        
        n = len(arr)
        res = n-1
        for i1 in range(firsti+1):
            while lastj < n and arr[lastj] < arr[i1]: lastj += 1
            print((i1, lastj))
            res = min(res, lastj - i1 - 1)
        
        return max(res, 0)

