class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if len(customers) == 0:
            return -1
        curWait = 0
        prof = 0
        maps = []
        count = 0
        while curWait != 0 or count < len(customers):
            if count < len(customers):
                cu = customers[count]
                curWait += cu
            count += 1
            prof -= runningCost
            if curWait <= 4:
                prof += curWait * boardingCost
                curWait = 0
            else:
                prof += 4 * boardingCost
                curWait -= 4
            maps.append([count, prof])
        maps = sorted(maps, key=lambda x: x[1], reverse=True)
        if maps[0][1] <= 0:
            return -1
        else:
            return maps[0][0]
