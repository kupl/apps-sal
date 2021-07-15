class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_ways = (amount+1) * [-1]
        num_ways[0] = 0
        
        for v in range(1, amount+1):
            fewest = float('inf')
            for c in coins:
                if v-c >= 0 and num_ways[v-c] != -1:
                    fewest = min(num_ways[v-c], fewest)
            if fewest != float('inf'):
                num_ways[v] = 1 + fewest
        
        return num_ways[amount]
