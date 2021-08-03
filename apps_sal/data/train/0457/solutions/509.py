class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 or not coins:
            return -1
        if not amount:
            return 0
        stack, lvl, visited = [0], 0, set()
        while stack:
            new_lvl = []
            lvl += 1
            for i in stack:
                for c in coins:
                    new = i + c
                    if new == amount:
                        return lvl
                    if new not in visited:
                        visited.add(new)
                        new_lvl.append(new)
            if min(new_lvl) > amount:
                return -1
            stack = new_lvl
