from functools import lru_cache


class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        @lru_cache(maxsize=100000)
        def dfs(s, n):
            if n == 0:
                return 1
            return sum([dfs(v, n - 1) for v in moves[s]])

        answer = 0
        for i in range(10):
            answer += dfs(i, N - 1)

        return answer % (10 ** 9 + 7)
