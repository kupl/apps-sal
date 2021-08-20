from collections import deque


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque()
        visited = set()
        queue.append((amount, 0))
        answer = -1
        while queue:
            (target, numCoins) = queue.popleft()
            if target == 0:
                answer = numCoins
                break
            elif target > 0:
                for coin in coins:
                    if target - coin not in visited:
                        visited.add(target - coin)
                        queue.append((target - coin, numCoins + 1))
        return answer
