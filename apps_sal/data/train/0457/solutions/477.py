class Solution:
    def coinChange(self, coins:List[int], amount:int) -> int:
        if amount == 0:
            return 0
        start = [0]
        visited = [False]*(amount+1)
        visited[0] = True
        numCoins = 1
        nextStart = []
        while start:
            for v in start:
                for coin in coins:
                    nextVal = v + coin
                    if nextVal > amount or visited[nextVal]:
                        continue
                    elif nextVal == amount:
                        return numCoins
                    else:
                        visited[nextVal] = True
                        nextStart.append(nextVal)
            start, nextStart = nextStart, []
            numCoins += 1
        return -1

