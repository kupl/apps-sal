class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [0] + [float('inf')] * amount
        for v in range(1, len(d)):
            for c in coins:
                if c <= v and d[v] > (d[v-c] + 1):
                    d[v] = d[v-c] + 1
        return d[-1] if d[-1] < float('inf') else -1

