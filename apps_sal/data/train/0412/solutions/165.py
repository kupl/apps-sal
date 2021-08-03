class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target == d or target == d * f:
            return 1
        T = [0 for i in range(target + 1)]
        m = 10**9 + 7
        T[0] = 1
        for i in range(0, d):
            for j in range(target, -1, -1):
                T[j] = 0
                for k in range(1, f + 1):
                    if j >= k:
                        T[j] += T[j - k] % m
                        T[j] %= m

        return T[target]
