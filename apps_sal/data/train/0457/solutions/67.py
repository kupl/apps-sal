class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeBFS(coins, amount)

    def coinChangeBFS(self, coins: List[int], amount: int) -> int:
        if amount == 0 or not coins:
            return 0
        queue = deque([amount])
        visited = set([amount])
        depth = 0
        while queue:
            length = len(queue)
            depth += 1
            for i in range(length):
                remaining = queue.popleft()
                for c in coins:
                    if remaining - c == 0:
                        return depth
                    elif remaining - c < 0:
                        continue
                    elif remaining - c not in visited:
                        queue.append(remaining - c)
                        visited.add(remaining - c)
        return -1
