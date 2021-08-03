class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]:
            return 1
        dp = [[0 for i in range(len(dungeon[0]))] for i in range(len(dungeon))]
        dp[-1][-1] = 1 - dungeon[-1][-1]
        row = len(dungeon)
        column = len(dungeon[0])
        for i in range(1, row):
            dp[row - 1 - i][-1] = max(1 - dungeon[row - 1 - i][-1], dp[row - i][-1] - dungeon[row - 1 - i][-1])
        for i in range(1, column):
            dp[-1][column - 1 - i] = max(1 - dungeon[-1][column - 1 - i], dp[-1][column - i] - dungeon[-1][column - 1 - i])
        for i in range(1, row):
            for j in range(1, column):
                dp[row - 1 - i][column - 1 - j] = max(1 - dungeon[row - 1 - i][column - 1 - j], min(dp[row - i][column - 1 - j], dp[row - 1 - i][column - j]) - dungeon[row - 1 - i][column - 1 - j])
        if dp[0][0] <= 0:
            return 1
        return dp[0][0]
        """
         :type dungeon: List[List[int]]
         :rtype: int
         """
