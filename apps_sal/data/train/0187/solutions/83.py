class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr=customers[0]
        onwheel=0
        i=1
        n=len(customers)
        cost=0
        ans=0
        while i<n or curr>0:
            if curr>=4:
                onwheel+=4
                temp=onwheel*boardingCost-i*runningCost
                if temp>cost:
                    cost=temp
                    ans=i
                if i<n:
                    curr+=(customers[i]-4)
                else:
                    curr-=4
                i+=1
            else:
                onwheel+=curr
                temp=onwheel*boardingCost-i*runningCost
                if temp>cost:
                    cost=temp
                    ans=i
                if i<n:
                    curr=customers[i]
                else:
                    curr=0
                i+=1
        return -1 if cost==0 else ans
