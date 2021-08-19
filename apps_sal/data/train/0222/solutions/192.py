class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        """
        dp(i, j): Maximum length of Fib sequence ending at A[i] & A[j]
        dp(i, j) = dp(k, j) + 1
        """
        cache = set(A)
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[j] - A[i] in cache and A[j] - A[i] < A[i]:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(list(dp.values()) + [0])
