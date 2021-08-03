from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(maxsize=None)
        def dfs(left, numConsecutive, last):
            total = 0
            if left == 0:
                if numConsecutive <= rollMax[last]:
                    return 1
                else:
                    return 0
            for i in range(6):
                if i == last:
                    if numConsecutive + 1 <= rollMax[last]:
                        total += dfs(left - 1, numConsecutive + 1, i)
                else:
                    total += dfs(left - 1, 1, i)
            return total

        return dfs(n, 0, -1) % (10**9 + 7)
