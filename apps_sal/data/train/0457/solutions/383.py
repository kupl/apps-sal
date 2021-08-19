class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        tracker = [float('inf') for i in range(amount)]
        res = self.coinChange_helper(coins, amount, tracker)
        print(tracker)
        if tracker[-1] == float('inf'):
            return -1
        return res

    def coinChange_helper(self, coins: List[int], amount: int, tracking: List[int]) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if tracking[amount - 1] != float('inf'):
            return tracking[amount - 1]
        lowest = float('inf')
        for i in range(len(coins)):
            result = self.coinChange_helper(coins, amount - coins[i], tracking)
            if result >= 0 and result + 1 < lowest:
                lowest = result + 1
        tracking[amount - 1] = lowest if lowest != float('inf') else -1
        return tracking[amount - 1]
