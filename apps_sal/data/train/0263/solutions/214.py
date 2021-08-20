class Solution:

    def initMoveTable(self):
        moveTable = dict()
        moveTable[0] = [4, 6]
        moveTable[1] = [6, 8]
        moveTable[2] = [7, 9]
        moveTable[3] = [4, 8]
        moveTable[4] = [0, 3, 9]
        moveTable[5] = []
        moveTable[6] = [0, 1, 7]
        moveTable[7] = [2, 6]
        moveTable[8] = [1, 3]
        moveTable[9] = [2, 4]
        return moveTable

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 10
        moveTable = self.initMoveTable()
        dp = []
        for i in range(n + 1):
            newRow = []
            for j in range(10):
                newRow.append(None)
            dp.append(newRow)
        for i in range(10):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(10):
                localNumWays = 0
                moves = moveTable[j]
                for move in moves:
                    localNumWays += dp[i - 1][move]
                dp[i][j] = localNumWays % (pow(10, 9) + 7)
        return sum(dp[i]) % (pow(10, 9) + 7)
