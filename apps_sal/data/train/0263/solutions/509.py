class Solution:

    def knightDialer(self, n: int) -> int:
        keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        dp = [[[1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]]
        modulo = 10 ** 9 + 7
        for k in range(1, n):
            dp.append([[0 for _ in range(3)] for _ in range(4)])
            for i in range(4):
                for j in range(3):
                    for (x, y) in [(i + 2, j + 1), (i + 2, j - 1), (i - 2, j + 1), (i - 2, j - 1), (i + 1, j + 2), (i + 1, j - 2), (i - 1, j + 2), (i - 1, j - 2)]:
                        if 0 <= x < 4 and 0 <= y < 3 and (keyboard[x][y] != -1):
                            dp[k][x][y] = (dp[k][x][y] + dp[k - 1][i][j]) % modulo
        return sum((sum(row) for row in dp[n - 1])) % modulo
