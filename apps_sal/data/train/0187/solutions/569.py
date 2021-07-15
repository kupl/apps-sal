class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        minimum = runningCost//boardingCost+1
        if minimum>4: return -1
        max_value = 0
        profit = 0
        remain = 0
        turns = 0
        res = None
        for c in customers:
            turns += 1
            temp = remain+c
            if temp>=4:
                remain = temp-4
                profit += 4*boardingCost-runningCost
            else:
                remain = 0
                profit += temp*boardingCost-runningCost
            if profit>max_value:
                res = turns
                max_value = profit
        print(turns, remain)
        while remain:
            turns += 1
            if remain>=4:
                remain -= 4
                profit += 4*boardingCost-runningCost
            else:
                profit += remain*boardingCost-runningCost
                remain = 0
            if profit>max_value:
                res = turns
                max_value = profit
        return res
