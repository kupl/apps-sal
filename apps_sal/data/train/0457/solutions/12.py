class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        queue = [(amount, 0)]
        visited = [False for i in range(amount + 1)]
        for val, cnt in queue:
            if val == 0:
                return cnt
            for coin in coins:
                if val - coin >= 0 and not visited[val - coin]:
                    visited[val - coin] = True
                    queue.append((val - coin, cnt + 1))
        return -1
