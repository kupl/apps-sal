class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def roll(i, j):
            if i == 0:
                return 1
            if i < 0:
                return 0
            cnt = 0
            for d in range(6):
                if d != j:
                    for k in range(rollMax[d]):
                        cnt = (cnt + roll(i - k - 1, d)) % MOD
            return cnt

        return roll(n, -1)
