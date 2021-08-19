class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])
