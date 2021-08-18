class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:
            return 0

        queue = deque([(0, 0)])
        visited = [True] + [False] * amount
        while queue:
            totalCoins, currVal = queue.popleft()
            totalCoins += 1
            for coin in coins:
                nextVal = currVal + coin
                if nextVal == amount:
                    return totalCoins

                if nextVal < amount:
                    if not visited[nextVal]:
                        visited[nextVal] = True
                        queue.append((totalCoins, nextVal))

        return -1
