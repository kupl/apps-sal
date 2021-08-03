class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not coins:
            return -1

        n = len(coins)

        if amount == 0:
            return 0

        fewest = [[0] * n for k in range(amount + 1)]

        for k in range(n):
            fewest[0][k] = 0

        for p in range(1, amount + 1):
            is_divisible = (p % coins[0]) == 0

            if is_divisible:
                fewest[p][0] = (p // coins[0])

            else:
                fewest[p][0] = -1

        for k in range(1, n):
            for p in range(1, amount + 1):
                if p < coins[k]:
                    fewest[p][k] = fewest[p][k - 1]

                elif fewest[p - coins[k]][k] == -1:
                    fewest[p][k] = fewest[p][k - 1]

                elif fewest[p][k - 1] == -1:
                    fewest[p][k] = fewest[p - coins[k]][k] + 1
                else:
                    fewest[p][k] = min(fewest[p - coins[k]][k] + 1, fewest[p][k - 1])

        return fewest[p][n - 1]
