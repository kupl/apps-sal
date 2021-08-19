class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        numbers = [float('inf')] * (amount + 1)
        numbers[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                numbers[x] = min(numbers[x], numbers[x - coin] + 1)
        return numbers[amount] if numbers[amount] < float('inf') else -1
