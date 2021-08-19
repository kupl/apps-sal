class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for (i, e) in enumerate(arr):
            k = e + -difference
            if k in d:
                d[e] = d[k] + 1
            if e not in d:
                d[e] = 1
        return d[max(d, key=lambda k: d[k])]
