class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0] * n for i in range(6)]
        m = 10**9 + 7
        for i in range(n):
            sum_ = 0
            for j in range(6):
                sum_ += dp[j][i - 1] % m
            sum_ = sum_ % m
            for j in range(6):
                if i == 0:
                    dp[j][i] = 1
                else:
                    if i + 1 <= rollMax[j]:
                        dp[j][i] = sum_
                    else:
                        s_ = 0
                        if i - rollMax[j] == 0:
                            dp[j][i] = sum_ - 1
                        else:
                            for k in range(6):

                                if k != j:
                                    s_ += dp[k][i - 1 - rollMax[j]] % m
                            s_ = s_ % m

                            dp[j][i] = sum_ - s_
        res = 0
        for i in range(6):
            res += dp[i][-1] % m
        return res % m
