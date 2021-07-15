class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = -1
        if not customers:
            return -1
        cnt = 1
        if customers[0] > 4:
            remain = customers[0] - 4
            p = 4
        else:
            p = customers[0]
            remain = 0
        profit = boardingCost * p - runningCost * cnt
        
        if profit > 0:
            res = cnt
            
        for num in customers[1:]:
            remain += num
            if remain > 4:
                remain -= 4
                p += 4
            else:
                p += remain
                remain = 0
            cnt += 1
            curr = boardingCost * p - runningCost * cnt
            
            if curr > profit:
                res = cnt
                profit = curr
        
        while remain > 0:
            
            if remain > 4:
                remain -= 4
                p += 4
            else:
                p += remain
                remain = 0
            cnt += 1
            curr = boardingCost * p - runningCost * cnt
            
            if curr > profit:
                res = cnt
                profit = curr
                
        return res

