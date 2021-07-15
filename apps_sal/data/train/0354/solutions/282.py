class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp, tmp, MOD = {}, {}, 10**9+7
        total, prev = [0] * 6, [0] * 6
        for k in range(n):
            for i in range(6):
                for j in range(1, rollMax[i]+1):
                    if j > 1:
                        tmp[(i, j)] = dp[(i, j-1)] if k > 0 else 0
                    else:
                        tmp[(i, j)] = (sum(prev) - prev[i]) % MOD if k > 0 else 1
                    total[i] += tmp[(i, j)]
            total, prev, dp, tmp = [0]*6, total, tmp, {}
        return sum(prev) % MOD
