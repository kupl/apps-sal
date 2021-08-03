class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = [0]
        visited = set()
        depth = 0
        while q:
            depth += 1
            level = []
            for curr in q:
                for coin in coins:
                    newvalue = curr + coin
                    if newvalue == amount:
                        return depth
                    if newvalue not in visited and newvalue < amount:
                        visited.add(newvalue)
                        level.append(newvalue)
            q = level
        return -1
