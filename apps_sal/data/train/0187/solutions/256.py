import sys
MIN_INT = -sys.maxsize-1
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        _max = MIN_INT
        rotate = 0
        ans = 0
        total = 0
        money = 0
        num = 0
        i = 0
        for i in range(len(customers)):
            total += customers[i]
            rotate = i+1
            if total >= 4:
                num += 4
                total -= 4
            else: 
                num += total
                total = 0
            money = num * boardingCost - rotate * runningCost
            if _max < money:
                _max = money
                ans = rotate
        i+=1
        while(total > 0):
            rotate = i+1
            if total >= 4:
                num += 4
                total -= 4
            else: 
                num += total
                total = 0
            money = num * boardingCost - rotate * runningCost
            if _max < money:
                _max = money
                ans = rotate
            i+=1
        if _max < 0: return -1
        return ans
