class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        best = [[0] * len(dungeon[0]) for x in range(0, len(dungeon))]
        for row in range(-1, -len(dungeon) - 1, -1):
            for col in range(-1, -len(dungeon[0]) - 1, -1):
                needed = -dungeon[row][col]
                nextSteps = []
                if row < -1:
                    nextSteps.append(best[row + 1][col])
                if col < -1:
                    nextSteps.append(best[row][col + 1])
                if len(nextSteps) > 0:
                    needed += min(nextSteps)
                needed = max(0, needed)
                best[row][col] = needed

        return best[0][0] + 1
