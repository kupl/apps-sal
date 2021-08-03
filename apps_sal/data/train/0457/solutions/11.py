from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = {0}
        tempQueue = deque()
        tempQueue.append((0, 0))
        while tempQueue:
            currentVal, currentCount = tempQueue.popleft()
            for coin in coins:
                nextVal = currentVal + coin
                if nextVal == amount:
                    return currentCount + 1
                elif nextVal < amount:
                    if nextVal not in visited:
                        visited.add(nextVal)
                        tempQueue.append((nextVal, currentCount + 1))
        return -1
