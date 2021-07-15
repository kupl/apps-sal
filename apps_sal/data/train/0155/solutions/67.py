from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @lru_cache(maxsize=None)
        def jump(i):
            res = 1

            def visit(rng):
                nonlocal res
                for j in rng:
                    if not 0 <= j < n or arr[j] >= arr[i]:
                        break
                    res = max(res, 1 + jump(j))

            visit(range(i - 1, i - d - 1, -1))
            visit(range(i + 1, i + d + 1))
            return res

        return max([jump(i) for i in range(n)])
