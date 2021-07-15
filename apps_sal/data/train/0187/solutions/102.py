class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        q = 0
        outs = []
        boarded = 0
        res = 0
        rots = 0
        m = 0
        for incoming in customers:
            if q + incoming > 4:
                q += incoming - 4
                boarded = 4
            else:
                boarded = q + incoming
                q = 0
            if len(outs) == 0:
                outs.append(boarded * boardingCost - runningCost)
            else:
                outs.append(outs[-1] + (boarded * boardingCost - runningCost))
            rots += 1
            if m < outs[-1]:
                m = outs[-1]
                res = rots
        
        while(q > 4):
            q -= 4
            outs.append(outs[-1] + (boarded * boardingCost - runningCost))
            rots += 1
            if m < outs[-1]:
                m = outs[-1]
                res = rots   
        outs.append(outs[-1] + (q * boardingCost - runningCost))
        rots += 1
        if m < outs[-1]:
            m = outs[-1]
            res = rots
        if m > 0:
            return res
        else:
            return -1
                
                
                
                

