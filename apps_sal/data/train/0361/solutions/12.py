from functools import lru_cache


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def backtrack(state):
            if state in cache:
                return cache[state]

            if min(state) == n:
                return 0

            temp = state
            state = list(state)
            min_size = min(state)
            start = state.index(min_size)
            res = max_area
            for end in range(start, m):
                if state[end] != min_size:
                    break
                size = end - start + 1
                if state[end] + size > n:
                    break
                state[start:end + 1] = [min_size + size] * size
                res = min(res, backtrack(tuple(state)))
            cache[temp] = res + 1
            return cache[temp]
        max_area = m * n
        cache = {}
        if m > n:
            m, n = n, m
        return backtrack((0,) * m)
