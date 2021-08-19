class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {(i, 1): 1 for i in range(6)}
        mod = 10 ** 9 + 7
        for _ in range(1, n):
            dp2 = {}
            for (r, t) in dp:
                for i in range(6):
                    if r == i:
                        if t == rollMax[i]:
                            continue
                        else:
                            dp2[r, t + 1] = dp[r, t] % mod
                    else:
                        dp2[i, 1] = (dp2.get((i, 1), 0) + dp[r, t]) % mod
            dp = dp2
        return sum(dp.values()) % mod
