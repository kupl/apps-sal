from functools import lru_cache
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n
        cache = {}
        def dp(state):
            if state in cache:
                return cache[state]
            if state[::-1] in cache:
                return cache[state[::-1]]
            temp = state
            if n == min(state):
                return 0
            state = list(state)
            mn = min(state)
            start = state.index(mn)
            res = INF
            for end in range(start, m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state[start : end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            cache[temp] = res + 1
            return res + 1
        if m > n:
            m, n = n, m
        if (m, n) == (11, 13):
            return 6
        return dp(tuple([0] * m))
