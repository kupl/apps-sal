class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = collections.defaultdict(lambda: 2)
        a = set(A)
        for j in range(2, len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in a:
                    dp[A[i], A[j]] = dp[A[j] - A[i], A[i]] + 1
        return max(dp.values() or [0])
