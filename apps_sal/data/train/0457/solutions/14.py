class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([])
        seen = set()
        coins = sorted(coins, reverse=True)
        queue.append((0, 0))
        while queue:
            (summ, num_coins) = queue.popleft()
            if summ == amount:
                return num_coins
            for coin in coins:
                if summ + coin <= amount and summ + coin not in seen:
                    queue.append((summ + coin, num_coins + 1))
                    seen.add(summ + coin)
        return -1
