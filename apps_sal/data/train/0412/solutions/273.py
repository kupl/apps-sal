from functools import lru_cache
MOD = 10 ** 9 + 7


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        sol = [0] * (target + 1)
        sol[0] = 1
        for _ in range(1, d + 1):
            nxt = [0] * (target + 1)
            for i in range(target + 1):
                (start, end) = (max(i - f, 0), i - 1)
                nxt[i] = sum(sol[start:end + 1]) % MOD
            sol = nxt
        return sol[target]
