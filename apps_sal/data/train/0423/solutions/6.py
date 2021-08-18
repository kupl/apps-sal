class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        d = dict()
        ret = 0
        for i, n in enumerate(arr):
            if n - difference not in d:
                d[n] = 1
            else:
                d[n] = d[n - difference] + 1

            ret = max(ret, d[n])
        return ret
