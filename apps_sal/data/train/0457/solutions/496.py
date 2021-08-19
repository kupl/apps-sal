import collections


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1, 2, 5], amount = 0
                       ^
                 2  3  6
                 4 
                 10
        """
        if not amount:
            return 0
        queue = collections.deque(coins)
        visited = set()
        count = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == amount:
                    return count
                for next in coins:
                    next += curr
                    if next not in visited and next <= amount:
                        visited.add(next)
                        queue.append(next)
            count += 1
        return -1
