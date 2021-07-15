class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < len(arr)-1 and arr[l+1] >= arr[l]:
            l +=1
        if l == len(arr)-1:
            return 0
        while r > 0 and arr[r-1] <= arr[r]:
            r -=1
        
        res = min(len(arr)-l-1, r)
        
        i, j = 0, r
        while i <= l and j < len(arr):
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i +=1
            else:
                j +=1
                
        return res

