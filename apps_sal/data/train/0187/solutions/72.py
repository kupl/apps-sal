class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        boarding = waiting = 0
        res = (0, 0)
        index = 1
        for (i, c) in enumerate(customers, 1):
            while index < i:
                if waiting >= 0:
                    boarding += min(waiting, 4)
                    waiting -= min(waiting, 4)
                cur = boardingCost * boarding - index * runningCost
                if res[0] < cur:
                    res = (cur, index)
                index += 1
            waiting += c
            prev = index
            while waiting >= 4:
                boarding += 4
                waiting -= 4
                cur = boardingCost * boarding - index * runningCost
                if res[0] < cur:
                    res = (cur, index)
                index += 1
        if waiting:
            boarding += waiting
            cur = boardingCost * boarding - index * runningCost
            if res[0] < cur:
                res = (cur, index)
        if res[0] > 0:
            return res[1]
        else:
            return -1
