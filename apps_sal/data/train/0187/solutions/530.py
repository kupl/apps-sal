class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        rotations = 0
        wheel = [0, 0, 0, 0]
        profits = []
        cost = 0
        waiting = 0
        profit = 0
        maxProfit = 0
        
        
        for i in range(len(customers)):
            waiting += customers[i]
            
            
            '''if rotations < i:
                for j in range(rotations - i):
                    profit -= runningCost
                    wheel[2], wheel[3] = wheel[1], wheel[2]
                    wheel[1] = 0'''
            
                
            if waiting > 4:
                profit += 4*boardingCost
            else:
                profit = boardingCost * waiting
            profit -= runningCost
            rotations += 1
            wheel[2], wheel[3] = wheel[1], wheel[2]
            wheel[1] = min(waiting, 4)
            waiting -= min(waiting, 4)
            profits.append((profit, rotations))
            
        while waiting > 0:
            profit += min(4, waiting) * boardingCost
            waiting -= min(4, waiting)
            profit -= runningCost
            rotations += 1
            profits.append((profit, rotations))
            
        #print(profits)
        profits = sorted(profits, key = lambda x: (x[0], -x[1]), reverse = True)
        if profits[0][0] > 0:
            return profits[0][1]
        else:
            return -1
