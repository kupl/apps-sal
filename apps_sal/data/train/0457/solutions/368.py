class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        for item in range(amount + 1):
            if (item < coins[0]) and item != 0:
                dp[item] = -1
            elif item == 0:
                dp[item] = 0

        if (amount < coins[0]) and amount == 0:
            return 0
        elif (amount < coins[0]):
            return -1

        for i in range(coins[0], amount + 1):
            count = 0

            for j in coins:
                if (i - j) < 0:
                    break
                elif dp[i - j] != -1:
                    count += 1
            if count > 0:
                dp[i] = math.ceil(i / coins[0])
                for j in coins:
                    if (i - j) < 0:
                        break
                    elif dp[i - j] == -1:
                        continue
                    else:
                        dp[i] = min(dp[i], 1 + dp[i - j])
            else:
                dp[i] = -1

        return dp[amount]
