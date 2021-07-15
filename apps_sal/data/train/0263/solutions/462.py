class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [[None] * 10 for _ in range(N + 1)]
        edges = [[1,6], [1,8], [2, 7], [2, 9],
                 [3, 4], [3, 8], [4, 9], [4, 0], 
                 [6, 7], [6, 0]]
        
        graph = {}
        for edge0, edge1 in edges:
            graph[edge0] = graph.get(edge0, []) + [edge1]
            graph[edge1] = graph.get(edge1, []) + [edge0]
            
        def count(n, x):
            if n == 0:
                return 1
            
            if dp[n][x] is not None:
                return dp[n][x]
            
            dp[n][x] = sum([count(n - 1, y) for y in graph.get(x, [])])
            return dp[n][x]
        
        return sum([count(N - 1, x) for x in range(10)]) % (10 ** 9 + 7)

