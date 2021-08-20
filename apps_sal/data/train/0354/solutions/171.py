class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modVal = 10 ** 9 + 7
        memo = {}

        def recurse(numLeft, prevNum, prevNumCount):
            if numLeft == 0:
                return 1
            if (numLeft, prevNum, prevNumCount) in memo:
                return memo[numLeft, prevNum, prevNumCount]
            numWays = 0
            for i in range(len(rollMax)):
                if i == prevNum:
                    if prevNumCount < rollMax[i]:
                        numWays += recurse(numLeft - 1, i, prevNumCount + 1)
                else:
                    numWays += recurse(numLeft - 1, i, 1)
            memo[numLeft, prevNum, prevNumCount] = numWays % modVal
            return numWays
        return recurse(n, -1, -1) % modVal
