class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        INF = m * n

        # I already have `state` filled. How many more squares do I need to build n * m?
        # @functools.lru_cache(None)
        def dp(state, memo):
            if state in memo:
                return memo[state]

            if n == min(state):
                return 0
            state_ = list(state)
            mn = min(state_)
            start = state_.index(mn)
            res = INF
            for end in range(start, m):
                if state[end] != mn:
                    break
                side = end - start + 1
                if mn + side > n:
                    break
                state_[start: end + 1] = [mn + side] * side
                res = min(res, dp(tuple(state_), memo) + 1)
            memo[tuple(state)] = res
            return res
        if m > n:
            m, n = n, m
        return dp(tuple([0] * m), {})
