class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n
        if m > n:
            (m, n) = (n, m)
        state = tuple([0] * m)

        @lru_cache(None)
        def dp(state):
            if min(state) == n:
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
                state[start:end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state)))
            return res + 1
        return dp(state)
