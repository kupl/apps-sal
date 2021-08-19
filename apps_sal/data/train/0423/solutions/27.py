from collections import defaultdict
import bisect


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
            next_indexes = mappings[arr[i] + difference]
            j = bisect.bisect_right(next_indexes, i)
            if j < len(next_indexes):
                M[i] += dp(next_indexes[j])
            return M[i]
        for i in range(n):
            ret = max(ret, dp(i))
        return ret
