class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[-math.inf] * K for _ in range(n)]
        sv, sc = 0, {-1: 0}
        for i, v in enumerate(A):
            sv += v
            sc[i] = sv
        dp[0][0] = A[0]
        for r in range(n):
            for i in range(0, r):
                for k in range(min(K, r + 1)):
                    if k == 0:
                        dp[r][k] = (sc[r] - sc[-1]) / (r + 1)
                    else:
                        candidate = dp[i][k - 1] + (sc[r] - sc[i]) / (r - i)
                        dp[r][k] = max(dp[r][k], candidate)
        # for row in dp:
        #     print(row)
        return dp[-1][-1]
