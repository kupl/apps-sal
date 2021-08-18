class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        q = deque()
        visited = set()
        q.append(amount)
        visited.add(amount)
        steps = 0
        while q:
            for _ in range(len(q)):
                poped = q.popleft()
                if poped == 0:
                    return steps
                for coin in coins:
                    new = poped - coin
                    if new not in visited and new >= 0:
                        q.append(new)
                        visited.add(new)

            steps += 1
        return -1
