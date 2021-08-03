class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][d]: the length of longest arithmetic d subsequence in A[:i]

        dp = [collections.defaultdict(lambda: 1) for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, i):
                d = A[i - 1] - A[j - 1]
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)

        return max(max(list(item.values()) or [1]) for item in dp)
