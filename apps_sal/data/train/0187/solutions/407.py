class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans = 0 
        rotations = 0
        n = len(customers)
        profit = 0 
        idx = 1
        rotation = 0
        curr_customers = customers[0]
        while curr_customers or idx<n:
            board = min(curr_customers,4)
            rotation += 1 
            profit += board*boardingCost - runningCost 
            curr_customers -= board
            if profit>ans:
                ans = profit
                rotations = rotation
            if idx<n:
                curr_customers += customers[idx] 
                rotation = max(rotation, idx) 
                idx+=1
        if rotations==0:
            return -1
        return rotations 
