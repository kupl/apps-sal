class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        def solve(n, last, last_count):
            if n == 0:
                return 1
            ans = 0
            for i in range(6):
                if i == last and last_count > 0:
                    ans += solve(n - 1, last, last_count - 1)
                elif i != last and rollMax[i] > 0:
                    ans += solve(n - 1, i, rollMax[i] - 1)
            return ans % MOD
        return solve(n, -1, -1)
