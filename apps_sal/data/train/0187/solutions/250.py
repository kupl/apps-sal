class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        
        if len(customers) == 0 or sum(customers) == 0:
            return 0
        
        revenue = 0
        costs = 0
        num_rotation = 0
        customers_waiting = 0
        profits = []
        
        
        while customers_waiting > 0 or num_rotation < len(customers):
            if num_rotation < len(customers):
                customers_waiting += customers[num_rotation]
            num_boarding = min(4, customers_waiting)
            customers_waiting -= num_boarding
            revenue += num_boarding * boardingCost
            costs += runningCost
            profits.append(revenue - costs)
            num_rotation += 1
        
        result = profits.index(max(profits))
        
        if profits[result] < 0:
            return -1
        
        return result+1
            
        
            
        
            
         
        
            
    
       
    
    
        
         
        

