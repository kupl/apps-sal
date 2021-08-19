class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        if n < 2:
            return 0
        res = 2
        dp = [{} for i in range(n)]
        dp[1] = {A[1] - A[0]: 2}
        for k in range(2, n):
            for i in range(k):
                diff = A[k] - A[i]
                if diff in dp[i]:
                    dp[k][diff] = dp[i][diff] + 1
                else:
                    dp[k][diff] = 2
        return max((max(item.values()) for item in dp if item))
