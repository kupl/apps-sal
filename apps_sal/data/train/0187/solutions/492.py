class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        import math
        n  = len(customers)
        s_ = sum(customers)
        last = 0
        profit = 0
        #times = (math.ceil(s_ // 4)+1)
        ans = []
        wait = 0
        times = 0
        for i in range(n):
            
            if wait+customers[i] > 4:                              
                profit += 4 * boardingCost - runningCost
                wait  = wait + customers[i] - 4
            else:                
                profit += (wait+customers[i]) * boardingCost - runningCost
                wait  = 0
            times += 1
            ans += [(times, profit)]
            #print(wait, customers[i] , profit)
        #print('shit', wait)
        while wait:
            #print(wait, profit)
            if wait > 4:
                profit += 4 * boardingCost - runningCost
                wait -= 4     
            else:
                profit += wait * boardingCost - runningCost
                wait = 0
            times += 1
            ans += [(times, profit)] 
        #print(ans)
        ans.sort(key=lambda x:(x[1], -x[0]))
        #print(ans)
        ans_t = ans[-1][0]
        ans_p = ans[-1][1]
        
        return  ans_t if ans_p >0 else -1
