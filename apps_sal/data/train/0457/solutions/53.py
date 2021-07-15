class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = [-1 for x in range(amount+1)]
        m[0] = 0
        coins = sorted(coins)
        if amount < min(coins):
            return m[amount]
        m[coins[0]] = 1
        for x in range(coins[0], amount+1):
            current_min = 10000000
            for y in coins:
                if y > x:
                    continue
                if m[x-y] < current_min and m[x-y] != -1:
                    current_min = m[x-y]
            if current_min == 10000000:
                m[x] = -1
            else:
                m[x] = current_min + 1
        print(m)
        return m[-1]
