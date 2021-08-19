class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        elif amount == 0:
            return 0
        coins.sort(reverse=True)
        visited = set()
        q = collections.deque([])
        for c in coins:
            if c == amount:
                return 1
            elif c < amount:
                q.append(c)
                visited.add(c)
        count = 1
        while q:
            size = len(q)
            count += 1
            for _ in range(size):
                prev = q.popleft()
                for c in coins:
                    cur = prev + c
                    if cur == amount:
                        return count
                    elif cur < amount and cur not in visited:
                        visited.add(cur)
                        q.append(cur)
        return -1
