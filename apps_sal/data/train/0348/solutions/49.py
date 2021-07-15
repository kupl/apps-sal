class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) < 0:
            return max(arr)
        
        memo = {}
        def recurse(idx, isSkipped):
            if idx == len(arr):
                return 0
            
            if (idx, isSkipped) in memo:
                return memo[(idx, isSkipped)]
            
            if isSkipped:
                memo[(idx, isSkipped)] = max(arr[idx] + recurse(idx + 1, True), 0)
            else:
                memo[(idx, isSkipped)] = max(arr[idx] + recurse(idx + 1, False), recurse(idx + 1, True), arr[idx])
                
            return memo[(idx, isSkipped)]
        
        curMax = float('-inf')
        for i in range(len(arr)):
            curMax = max(recurse(i, False), curMax)

        return curMax
