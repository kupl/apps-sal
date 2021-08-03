class Solution:
    def knightDialer(self, n: int) -> int:
        graph = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [6, 2], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        @lru_cache(None)
        def dfs(node, n=n):
            if n == 1:
                return 1
            else:
                moves = 0
                for neigb in graph[node]:
                    # if neigb in (3, 6, 9):
                    #     neigb -= 2
                    moves += dfs(neigb, n - 1)
                return moves

        ans = 0
        for node in range(10):
            ans += dfs(node)

        return ans % (10 ** 9 + 7)
