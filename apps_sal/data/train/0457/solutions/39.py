class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        queue = deque()
        numCoins = 0
        seen = set()
        coins.sort(reverse=True)
        queue.append(amount)

        if amount == 0:
            return 0

        while queue:
            qlen = len(queue)
            numCoins += 1
            for i in range(qlen):
                x = queue.popleft()
                for coin in coins:
                    if x - coin == 0:
                        return numCoins
                    elif x - coin > 0:
                        if x - coin not in seen:
                            queue.append(x - coin)
                            seen.add(x - coin)
        return -1
