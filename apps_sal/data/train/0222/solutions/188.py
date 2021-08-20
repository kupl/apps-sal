from collections import defaultdict


class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        maps = {num: i for (i, num) in enumerate(A)}
        n = len(A)
        dp = defaultdict(lambda: 2)
        max_len = 0
        for i in range(2, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in maps and diff < A[j]:
                    idx = maps[diff]
                    dp[j, i] = max(dp[j, i], dp[idx, j] + 1)
                    max_len = max(dp[j, i], max_len)
        return max_len if max_len > 2 else 0
