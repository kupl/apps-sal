from collections import deque


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        queue = deque([])
        for coin in coins:
            if amount - coin >= 0:
                queue.append((1, amount - coin))
        seen = set()
        while queue:
            nex = queue.popleft()
            if nex[1] == 0:
                return nex[0]
            for coin in coins:
                if nex[1] - coin not in seen and nex[1] - coin >= 0:
                    queue.append((nex[0] + 1, nex[1] - coin))
                    seen.add(nex[1] - coin)
        return -1
