class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        myQueue = [[0,0]]
        reachedMap = {0}
        for value, num_coins in myQueue:
            for coin in coins:
                if coin+value in reachedMap:
                    continue
                if coin + value == amount:
                    return num_coins + 1
                if coin+value < amount:
                    reachedMap.add(value+coin)
                    myQueue.append([coin+value, num_coins + 1])
        return -1

