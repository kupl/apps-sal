class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = [0]
        depth = 0
        visited = set()
        while q:
            level = []
            depth += 1
            for curr in q:
                for coin in coins:
                    newvalue = curr + coin
                    if newvalue == amount:
                        return depth
                    elif newvalue not in visited and newvalue < amount:
                        visited.add(newvalue)
                        level.append(newvalue)
            q = level
        return -1
