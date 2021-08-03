class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        m = len(dungeon[0])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i + 1 < n and j + 1 < m:
                    temp = max(dungeon[i + 1][j], dungeon[i][j + 1])
                elif i + 1 < n:
                    temp = dungeon[i + 1][j]
                elif j + 1 < m:
                    temp = dungeon[i][j + 1]
                else:
                    temp = 0
                print(temp)
                dungeon[i][j] = dungeon[i][j] + temp
                dungeon[i][j] = min(dungeon[i][j], 0)
        return(max(1, 1 - dungeon[0][0]))
