class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res = 0
        q = 0
        u = 0
        profit = 0
        rotation = 0
        
        for c in customers:
            rotation += 1
            if c > 4:
                q += c - 4
                u += 4
            else:
                if q > 0:
                    diff = 4 - c
                    if q >= diff:   
                        u += c + diff
                        q -= diff
                    else:
                        u += c + q
                        q = 0
                else:
                    u += c
            
            if profit < u * boardingCost - rotation * runningCost:
                profit = u * boardingCost - rotation * runningCost
                res = rotation
        
        while q > 0:
            rotation += 1
            if q > 4:
                u += 4
                q -= 4
            else:
                u += q
                q = 0
            if profit < u * boardingCost - rotation * runningCost:
                profit = u * boardingCost - rotation * runningCost
                res = rotation
            
        print(profit)
        return res if profit > 0 else -1
                

