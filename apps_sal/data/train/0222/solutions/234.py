class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        s = set(A)
        n = len(A)
        ans = 2
        for j in range(n):
            for i in range(j):
                prev = A[j] - A[i]
                if prev < A[i] and prev in s:
                    dp[A[i], A[j]] = dp.get((prev, A[i]), 2) + 1
        return max(list(dp.values()) or [0])
