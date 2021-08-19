class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        DP = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(f + 1):
            if i <= target:
                DP[1][i] = 1
        if d == 1:
            return DP[d][target]
        for j in range(2, d + 1):
            for i in range(1, target + 1):
                for val in range(1, f + 1):
                    if 0 < i - val < len(DP[j]):
                        DP[j][i] += DP[j - 1][i - val]
        return DP[d][target] % (10 ** 9 + 7)
