class Solution2:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * 501 for i in range(n)]
        max_val = 0
        for i in range(n):
            for j in range(i):
                dif = A[i] - A[j]
                dp[i][dif] = max(dp[i][dif], dp[j][dif] + 1)
                max_val = max(dp[i][dif], max_val)
        return max_val + 1


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(dict)
        max_val = 0
        for i in range(n):
            for j in range(i):
                dif = A[i] - A[j]
                dp[dif].setdefault(i, 0)
                dp[dif][i] = dp[dif].get(j, 0) + 1
                max_val = max(dp[dif][i], max_val)
        return max_val + 1


class Solution1:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [collections.defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(0, i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
        return res + 1
