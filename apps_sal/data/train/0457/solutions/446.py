import queue


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = queue.Queue()
        q.put(amount)
        q.put(None)
        level = 0
        visited = {amount}
        while not q.empty():
            num = q.get()
            if num is None:
                if q.empty():
                    break
                q.put(None)
                level += 1
                continue
            for coin in coins:
                if num - coin > 0 and (num - coin) not in visited:
                    q.put(num - coin)
                    visited.add(num - coin)
                elif num - coin == 0:
                    return level + 1

        return -1
