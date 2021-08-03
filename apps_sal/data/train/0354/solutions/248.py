from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.rollMax = rollMax
        return self.solve(n, -1, 0) % (1000000007)

    @lru_cache(maxsize=4096 * 2, typed=False)
    def solve(self, n, last_index=-1, last_times=0):
        if n == 0:
            return 1
        else:
            res = 0
            for i in range(6):
                if i == last_index and self.rollMax[i] > last_times:
                    res += self.solve(n - 1, i, last_times + 1)
                elif i != last_index:
                    res += self.solve(n - 1, i, 1)

            return res
