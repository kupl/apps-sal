class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        d = dict()
        res = 1
        for i in arr:
            if i - diff in d.keys():
                d[i] = 1 + d[i - diff]
            else:
                d[i] = 1
            res = max(res, d[i])
        return res
