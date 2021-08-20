class Solution:

    def catMouseGame(self, graph):
        import functools
        n = len(graph)

        @lru_cache(None)
        def dp(t, x, y):
            if t == 2 * n:
                return 0
            if x == y:
                return 2
            if x == 0:
                return 1
            if t % 2 == 0:
                if any((dp(t + 1, xn, y) == 1 for xn in graph[x])):
                    return 1
                if all((dp(t + 1, xn, y) == 2 for xn in graph[x])):
                    return 2
                return 0
            else:
                if any((dp(t + 1, x, yn) == 2 for yn in graph[y] if yn != 0)):
                    return 2
                if all((dp(t + 1, x, yn) == 1 for yn in graph[y] if yn != 0)):
                    return 1
                return 0
        return dp(0, 1, 2)
