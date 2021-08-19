from collections import defaultdict


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        ret = 0
        mappings = defaultdict(list)
        for (i, v) in enumerate(arr):
            mappings[v].append(i)
        M = [-1 for i in range(n)]

        def dp(i):
            if i == n - 1:
                return 1
            if M[i] != -1:
                return M[i]
            M[i] = 1
            for j in mappings[arr[i] + difference]:
                if j > i:
                    M[i] += dp(j)
                    break
            return M[i]
        for i in range(n):
            ret = max(ret, dp(i))
        return ret
