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
        return dp(tuple([0] * m))
        @lru_cache
        def backtrack(state):
            if n == min(state):
                return 0
            
            state = list(state)
            state_min = min(state)
            start = state.index(state_min)
            res = area
            for end in range(start, m):
                if state[end] != state_min:
                    break
                side = end - start + 1
                if state_min + side > n:
                    break
                state[start:end+1] = [state_min+side] * side
                res = min(res, backtrack(tuple(state)))
            return res + 1
        
        if m > n:
            m, n = n, m
        area = n * m
        return backtrack(tuple([0] * m))
