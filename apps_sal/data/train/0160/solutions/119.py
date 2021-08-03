class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        table = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            table[i][i] = True

        for row in range(n - 1, -1, -1):
            for col in range(row, n + 1):
                if table[row][col - 1] == False:
                    table[row][col] = True
                if table[row + 1][col] == False:
                    table[row][col] = True
        return table[0][n]
