class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp template 2: number of paths

        cache = {}
        MOD = 10**9 + 7

        def dp(n: int, prev_roll: int, prev_count: int) -> int:
            if n == 0:
                return 1

            if (n, prev_roll, prev_count) in cache:  # store state
                return cache[n, prev_roll, prev_count]

            res = 0
            for i in range(len(rollMax)):
                if prev_roll != None and i == prev_roll:
                    if prev_count == rollMax[i]:  # can't be more than rollMax[i] consecutive times
                        continue
                    res += dp(n - 1, i, prev_count + 1)
                else:
                    res += dp(n - 1, i, 1)

            cache[n, prev_roll, prev_count] = res % MOD
            return res % MOD

        return dp(n, None, None)
