class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def dp(state):
            if state in cache:
                return cache[state]
            if state[::-1] in cache:
                return cache[state[::-1]]
            tmp = state
            if min(state) == n:
                return 0
            state = list(state)
            min_s = min(state)
            start = state.index(min_s)
            res = n
            for end in range(start, m):
                if state[end] != min_s:
                    break
                side = end - start + 1
                if min_s + side > n:
                    break
                state[start: end + 1] = [min_s + side] * side
                res = min(res, dp(tuple(state)))
            cache[tmp] = res + 1
            return res + 1

        if m > n:
            m, n = n, m
        cache = dict()
        return dp(tuple([0] * m))
