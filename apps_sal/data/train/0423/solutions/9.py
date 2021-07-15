class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = {} 
        for num in arr:
            if num - difference in res:
                res[num] = res[num - difference] + 1 
            else:
                res[num] = 1
        return max(res.values())
