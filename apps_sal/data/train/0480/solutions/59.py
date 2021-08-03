class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = dict()

        def calculateWays(steps, arrLen, index):
            if index < 0 or index >= arrLen:
                return 0
            elif steps == 0 and index == 0:
                return 1
            elif steps == 0 and index != 0:
                return 0
            elif (steps, index) in memo:
                return memo[(steps, index)]
            else:
                goLeft = calculateWays(steps - 1, arrLen, index - 1)
                stay = calculateWays(steps - 1, arrLen, index)
                goRight = calculateWays(steps - 1, arrLen, index + 1)
                memo[(steps, index)] = goLeft + stay + goRight
                return memo[(steps, index)]

        return calculateWays(steps, arrLen, 0) % (10**9 + 7)
