class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n <= 1:
            return A
        t = collections.defaultdict(int)
        dp = [None] * n
        for i in range(n):
            dp[i] = collections.defaultdict(int)
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j][diff] + 1
        ret = 0
        for i in range(n):
            ret = max(ret, max(dp[i].values()) + 1)
        return ret
