class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        prev = 0
        nb = 0
        tw = sum(customers)
        nw = 0
        ans = 0
        total = 0
        i = 0
        res = -1
        
        #print(tw)
        while (i <n) or (nw != 0):
            if i >= n:
                nb = nw
            else :
                nb  = nw + customers[i]
            
            if nb >= 4:
                nw = nb -4
                nb = 4
            else :
                nw = 0
                
            total += nb
            if (total * boardingCost - (i+1) * runningCost) > ans:
                res = i+1
            ans = max(total * boardingCost - (i+1) * runningCost, ans)
            #print(i+1, ans)
            
            i += 1
        return res
