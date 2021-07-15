class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = -1
        if boardingCost * 4 < runningCost: return ans
        cur_profit = 0
        wait_num = 0
        dic = {}
        for i in range(len(customers)):
            if customers[i] + wait_num < 5:
                cur_profit += boardingCost * (customers[i] + wait_num) - runningCost
                wait_num = 0
            else:
                cur_profit += boardingCost * 4 - runningCost
                wait_num += customers[i] - 4
                
            if cur_profit > ans:
                ans = cur_profit
                dic[ans] = i+1
        
        if wait_num > 0:
            while wait_num > 3:
                wait_num -= 4
                dic[ans] += 1
            if wait_num * boardingCost > runningCost:
                dic[ans] += 1
        
        return dic[ans]

