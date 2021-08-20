class Solution:

    def coinChange(self, coins, amount):
        coins.sort()
        stack = [(0, 0, len(coins))]
        min_steps = 2 ** 31
        while len(stack) != 0:
            (steps, accumulated, sequence) = stack.pop()
            if accumulated == amount:
                min_steps = min(min_steps, steps)
            if accumulated > amount or amount - accumulated > coins[sequence - 1] * (min_steps - steps):
                continue
            for (seq, coin) in enumerate(coins[:sequence]):
                stack.append((steps + 1, accumulated + coin, seq + 1))
        return min_steps if min_steps != 2 ** 31 else -1
