class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def dp(pos, last, numlast):
            if pos == n:
                return 1
            res = 0
            for i in range(1, 7):
                if i != last:
                    res += dp(pos + 1, i, 1)
                elif numlast < rollMax[i - 1]:
                    res += dp(pos + 1, last, numlast + 1)
            return res
        return dp(0, 0, 0) % (10 ** 9 + 7)
