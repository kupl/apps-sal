class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        res = 0
        for i in arr:
            if i - difference in d:
                d[i] = 1 + d.pop(i - difference)
            elif i not in d:
                d[i] = 1
            res = max(res, d[i])
        return res
