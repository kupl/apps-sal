class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not coins and amount:
            return -1

        if not amount:
            return 0

        target = [0] * (amount + 1)
        target[0] = 1

        # coins[::-1].sort()

        for i in range(len(coins) - 1, -1, -1):

            coin = coins[i]
            j = 0
            while j <= amount:

                if target[j] == 0:
                    j += 1
                    continue

                next_idx = j + coin
                if next_idx > amount:
                    break

                if target[j] > 0 and (target[next_idx] > target[j]) or target[next_idx] == 0:
                    target[next_idx] = target[j] + 1

                j += 1

        print(target)
        if target[amount]:
            return target[amount] - 1
        else:
            return -1
