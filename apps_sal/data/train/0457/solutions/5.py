class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = [[amount, 0]]
        visited = set()
        for q in queue:
            for c in coins:
                if q[0] - c in visited:
                    continue
                if q[0] == c:
                    return q[1] + 1
                if q[0] > c:
                    visited.add(q[0] - c)
                    queue.append([q[0] - c, q[1] + 1])
        return -1
