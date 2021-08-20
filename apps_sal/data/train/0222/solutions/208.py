from collections import defaultdict


class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = defaultdict(int)
        s = set(A)
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in s:
                    dp[A[i], A[j]] = dp.get((A[j], A[i] - A[j]), 2) + 1
        return max(dp.values()) if dp else 0
