class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if len(customers)==0:
            return -1
        wait = 0
        onboard = 0
        r=0
        max_prof, max_r, cost = float('-inf'),0,0
        while customers[r] == 0:
            r+=1
            
        if customers:
            wait+=customers[r]
            while wait >0:
                c = min(wait, 4)
                wait = max(0, wait-4)
                onboard+=c
                r+=1
                cost = onboard*boardingCost - r*runningCost
                if cost >max_prof:
                    max_r = r
                    max_prof = cost
                if r<len(customers):
                    wait+=customers[r]
                # if wait <10:
                #     print(cost, r, wait, onboard)

        if max_prof <=0:
            return -1
        return max_r
            

