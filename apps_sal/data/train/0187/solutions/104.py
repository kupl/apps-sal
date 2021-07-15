class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        cur = 0
        ans = 0
        for c in customers:
            cur += c
            if cur >= 4:
                cur -= 4
            elif cur > 0:
                cur = 0

        ans = len(customers)+cur//4
        if cur%4*boardingCost > runningCost:
            ans += 1
        
        if 4*boardingCost < runningCost:
            return -1
        
        return ans
        

