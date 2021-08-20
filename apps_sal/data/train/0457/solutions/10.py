class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        if amount == 0:
            return 0
        q = [(amount, 0)]
        visited = {0}
        coins.sort(reverse=True)
        while q:
            (node, depth) = q.pop(0)
            for coin in coins:
                rest = node - coin
                if rest == 0:
                    return depth + 1
                if rest > 0 and rest not in visited:
                    q.append((rest, depth + 1))
                    visited.add(rest)
        return -1
