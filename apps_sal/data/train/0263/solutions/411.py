class Solution:
    def knightDialer(self, n: int) -> int:

        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 9, 3], 5: [], 6: [0, 7, 1], 7: [2, 6], 8: [1, 3], 9: [4, 2]}
        ans = 0
        self.cache = {}
        for u in list(graph.keys()):
            ans += self.dial(graph, u, n - 1)

        return ans % (10**9 + 7)

    def dial(self, graph, start, n):

        if n == 0:
            return 1

        ans = 0

        key = str(start) + ' ' + str(n)

        if key in list(self.cache.keys()):

            return self.cache[key]

        for v in graph[start]:
            ans += self.dial(graph, v, n - 1)

        self.cache[key] = ans

        return self.cache[key]
