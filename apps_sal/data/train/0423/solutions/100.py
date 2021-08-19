class Solution:

    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        d = dict()
        res = 1
        for i in arr:
            t = 0
            try:
                t = d[i - diff]
            except:
                pass
            if t:
                d[i] = 1 + d[i - diff]
            else:
                d[i] = 1
            res = max(res, d[i])
        return res
