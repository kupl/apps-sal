# DP, either recursion or iteration works (recursion is faster than iteration, O(dt) vs. O(dft))
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                if i == 1:
                    if 1 <= j <= f:
                        memo[i][j] = 1
                    continue
                for t in range(1, f + 1):
                    if j >= t:
                        memo[i][j] += memo[i - 1][j - t]
        return memo[d][target] % (10 ** 9 + 7)
