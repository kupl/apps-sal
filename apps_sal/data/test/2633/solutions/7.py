class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        record = [[None] * n for i in range(m)]
        record[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(n - 1)[::-1]:
            record[m - 1][i] = max(1, record[m - 1][i + 1] - dungeon[m - 1][i])
        for j in range(m - 1)[::-1]:
            record[j][n - 1] = max(1, record[j + 1][n - 1] - dungeon[j][n - 1])

        for i in range(m - 1)[::-1]:
            for j in range(n - 1)[::-1]:
                mina = max(record[i + 1][j] - dungeon[i][j], 1)
                minb = max(record[i][j + 1] - dungeon[i][j], 1)
                record[i][j] = min(mina, minb)
        return record[0][0]
