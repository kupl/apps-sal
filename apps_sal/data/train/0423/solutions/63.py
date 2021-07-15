class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        mx = 1

        for i, e in enumerate(arr):
            k = e + -difference

            if k in d:
                d[e] = d[k] + 1
                mx = max(mx, d[e])

            if e not in d:
                d[e] = 1

        return mx
