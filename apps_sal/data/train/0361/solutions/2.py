from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n

        # I already have state filled, how many more squares do I need to build a n*m?
        @lru_cache(None)
        def dp(state):
            if n == min(state):  # all filled
                return 0
            state = list(state)
            mn = min(state)
            start = state.index(mn)
            res = INF
            for end in range(start, m):
                if state[end] != mn:  # if not in the lowest point, break
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start:end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            return res + 1  # res is filled, +1 means the current dp

        if m > n:
            m, n = n, m
        return dp(tuple([0] * m))
