class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        curr = [float('inf')]*(amount+1)
        curr[0] = 0
        coins = sorted(coins)
        for num in range(amount+1):
            for c in coins:
                if num-c < 0: break
                curr[num] = min(curr[num], curr[num-c]+1)
        return curr[amount] if curr[amount]<float('inf') else -1
            

