class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        waysDict = {}
        return self.numWaysRec(steps, arrLen, 0, waysDict) % (10**9 + 7)

    def numWaysRec(self, steps: int, arrLen: int, currentPos: int, waysDict: dict) -> int:
        if (steps == currentPos) or (steps == 1 and currentPos == 0):
            return 1
        totalWays = 0
        for nextMove in self.validMoves(steps, currentPos, arrLen):
            if (nextMove, steps - 1) in waysDict:
                totalWays += waysDict[(nextMove, steps - 1)]
            else:
                result = self.numWaysRec(steps - 1, arrLen, nextMove, waysDict)
                waysDict[(nextMove, steps - 1)] = result
                totalWays += result
        return totalWays

    def validMoves(self, steps: int, currentPos: int, arrLen: int) -> list:
        validList = []
        # Check left move
        if (currentPos - 1 <= steps - 1) and currentPos - 1 >= 0:
            validList.append(currentPos - 1)
        # Check stay move
        if (currentPos <= steps - 1):
            validList.append(currentPos)
        # Check right move
        if (currentPos + 1 <= steps - 1) and currentPos + 1 < arrLen:
            validList.append(currentPos + 1)

        return validList
