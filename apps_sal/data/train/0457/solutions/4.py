class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:  # Don't need any coin.
            return 0

        queue = deque([(0, 0)])
        visited = [True] + [False] * amount
        while queue:
            totalCoins, currVal = queue.popleft()
            totalCoins += 1  # Take a new coin.
            for coin in coins:
                nextVal = currVal + coin
                if nextVal == amount:  # Find a combination.
                    return totalCoins

                if nextVal < amount:  # Could add more coins.
                    if not visited[nextVal]:  # Current value not checked.
                        visited[nextVal] = True  # Prevent checking again.
                        queue.append((totalCoins, nextVal))

        return -1  # Cannot find any combination.
