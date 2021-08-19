class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        maxAmount = 10 ** 9 + 7
        '\n        dp[d][v] = dp[d-1][v-1] + dp[d-1][v-2] + ... + dp[d-1][v-f]\n        '
        if target < 1 or d * f < target:
            return 0
        dpPrev = [(i, 1) for i in range(1, f + 1)]
        for roundNo in range(2, d + 1):
            numWays = defaultdict(int)
            for (i, v) in dpPrev:
                for num in range(1, f + 1):
                    numWays[i + num] += v
            dpPrev = []
            for k in numWays:
                dpPrev.append((k, numWays[k]))
        for pair in dpPrev:
            if pair[0] == target:
                return pair[1] % maxAmount
        return 0
