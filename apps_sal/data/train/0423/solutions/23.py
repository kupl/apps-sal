class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        if len(arr) == 1:
            return 1
        memo = {}
        res = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i]+difference not in memo:
                memo[arr[i]] = 1
            else:
                memo[arr[i]] = memo[arr[i]+difference] + 1
            
            res = max(res, memo[arr[i]])
        return res
            
        

