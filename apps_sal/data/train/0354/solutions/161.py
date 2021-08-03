import functools as ft


class Solution:

    BASE = 10 ** 9 + 7

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.roll_max = rollMax
        return self.count(n, 1, 0)

    @ft.lru_cache(None)
    def count(self, remaining: int, last_roll: int, streak: int) -> int:
        if remaining == 0:
            return 1
        ans = 0
        for dice in range(1, 7):
            if dice == last_roll:
                if streak >= self.roll_max[last_roll - 1]:
                    continue
                ans += self.count(remaining - 1, dice, streak + 1)
            else:
                ans += self.count(remaining - 1, dice, 1)
        return ans % self.BASE
