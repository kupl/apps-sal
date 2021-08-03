class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1

        m = len(dungeon)
        n = len(dungeon[0])

        dp = [None] * n

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                tmp = []
                if i + 1 < m:
                    tmp.append(dp[j])

                if j + 1 < n:
                    tmp.append(dp[j + 1])

                minLeft = 1
                if tmp:
                    minLeft = min(tmp)

                dp[j] = max(minLeft - dungeon[i][j], 1)

        return dp[0]
