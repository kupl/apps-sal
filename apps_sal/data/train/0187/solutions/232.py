class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # 4 gondalas, each gondola can sit up to 4 people
        # rotates counterclockwise, costs 'runningCost'
        
        # customers[i] is the number of new customers arriving before the ith rotation
        if 4*boardingCost <= runningCost: return -1
        
        remain = 0
        for i,c in enumerate(customers):
            if c == 4 or (c < 4 and remain == 0):
                continue
            if c < 4:
                if c + remain <= 4:
                    c += remain
                    remain = 0
                    customers[i] = c
                else:
                    # get new remain
                    remain -= (4 - c)
                    customers[i] = 4
            else:
                # collect remain
                remain += (c - 4)
                customers[i] = 4
        
        sofar = 0
        hi = 0
        hiInd = -1
        for i,c in enumerate(customers):
            sofar += (c * boardingCost - runningCost)
            if sofar > 0 and sofar > hi:
                hi = sofar
                hiInd = i + 1
        
        rounds = remain // 4
        extra = remain % 4
        
        sofar += rounds*(4*boardingCost - runningCost)
        if sofar > 0 and sofar > hi:
            hi = sofar
            hiInd = len(customers) + rounds
        sofar += (extra*boardingCost - runningCost)
        if sofar > 0 and sofar > hi:
            hiInd += 1
        
        return hiInd
