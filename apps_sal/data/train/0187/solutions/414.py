class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        maxx=0
        kotae=-1
        num=customers[0]
        current=0
        count=1
        
        while num>0 or count<len(customers):
            on=min(num,4)
            num-=on
            
            current+=on*boardingCost
            current-=runningCost
            
            if current>maxx:
                maxx=current
                kotae=count
            if count<len(customers):
                num+=customers[count]
            count+=1
            
            # print(current,kotae)
            
        return kotae
