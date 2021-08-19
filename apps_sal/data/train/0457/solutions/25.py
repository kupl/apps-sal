from collections import deque


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque()
        q.append([amount, 0])
        level = 0
        seen = set()
        while q:
            (amt, level) = q.popleft()
            for n in coins:
                if amt - n == 0:
                    return level + 1
                if amt - n in seen or amt - n < 0:
                    continue
                seen.add(amt - n)
                q.append([amt - n, level + 1])
        return -1
