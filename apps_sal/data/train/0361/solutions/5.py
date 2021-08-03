from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        @lru_cache(None)
        def dfs(state):
            if n == min(state):
                return 0
            state = list(state)
            minimum = min(state)
            start = state.index(minimum)
            res = inf
            for end in range(start, m):
                if state[end] != minimum:
                    break
                side = end - start + 1
                if minimum + side > n:
                    break
                state[start:end + 1] = [minimum + side] * side
                res = min(res, dfs(tuple(state)))
            return res + 1

        inf = m * n
        if m > n:
            m, n = n, m
        return dfs(tuple([0] * m))
