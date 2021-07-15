class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        self.customers = customers
        self.boardingCost = boardingCost
        self.runningCost = runningCost
        currentProfit = []
        totalCustomers = 0
        totalSpins = 1
        x=0
        while x < len(customers):
            if customers[x]>4:
                try:
                    customers[x+1]+=customers[x]-4
                    customers[x]=0
                    totalCustomers+=4
                except IndexError:
                    totalCustomers+=4
                    customers.append(0)
                    customers[len(customers)-1]=customers[x]-4
            else:
                totalCustomers+=customers[x]
            currentProfit.append(totalCustomers*boardingCost-totalSpins*runningCost)
            totalSpins+=1
            x+=1
        temp_highest = -21749271
        a=0
        y=0
        for element in currentProfit:
            if element>temp_highest:
                temp_highest=element
                a=y
            y+=1
        
        if temp_highest<0:
            return -1
        else:
            return a+1
                
                
                
                

