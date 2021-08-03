class Solution:
    def catMouseGame(self, graph):

        from functools import lru_cache
        N = len(graph)

        @lru_cache(None)
        def search(t, x, y):
            if t == 2 * N:
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            if (t % 2 == 0):
                if any(search(t + 1, xn, y) == 1 for xn in graph[x]):
                    return 1
                if all(search(t + 1, xn, y) == 2 for xn in graph[x]):
                    return 2
                return 0
            else:
                if all(search(t + 1, x, yn) == 1 for yn in graph[y] if yn != 0):
                    return 1
                if any(search(t + 1, x, yn) == 2 for yn in graph[y] if yn != 0):
                    return 2
                return 0
        return search(0, 1, 2)
