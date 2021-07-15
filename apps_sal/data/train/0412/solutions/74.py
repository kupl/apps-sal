MOD = 10 ** 9 + 7

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        ways = [0] + [1] * min(f, target) + [0] * max(target - f, 0)
        for _ in range(d - 1):
            for i in reversed(range(1, target + 1)):
                ways[i] = 0
                for j in range(1, min(i, f + 1)):
                    ways[i] = (ways[i] + ways[i - j]) % MOD
        return ways[target]
