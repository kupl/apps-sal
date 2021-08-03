class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.mod = 10 ** 9 + 7

        return self.dp(arrLen, steps, 0)

    @lru_cache(None)
    def dp(self, n, steps, i):
        if steps == 0 and i == 0:
            return 1

        if i >= n or i < 0 or steps == 0:
            return 0

        stay_in_place = self.dp(n, steps - 1, i)
        move_left = self.dp(n, steps - 1, i - 1)
        move_right = self.dp(n, steps - 1, i + 1)

        return (stay_in_place + move_left + move_right) % self.mod
