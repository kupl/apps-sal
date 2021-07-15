import functools
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n
        
        # state store height at each column, we'll cache this state
        @functools.lru_cache(None)
        def dp(state):
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
            return res + 1
        if m > n:
            m, n = n, m
        return dp(tuple([0] * m))
