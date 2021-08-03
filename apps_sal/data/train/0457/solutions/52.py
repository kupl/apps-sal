class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = [[amount, 0]]
        visited = {0}
        for q in queue:
            for c in coins:
                if q[0] == c:
                    return q[1] + 1
                elif q[0] > c and q[0] - c not in visited:
                    visited.add(q[0] - c)
                    queue.append([q[0] - c, q[1] + 1])
        return -1
