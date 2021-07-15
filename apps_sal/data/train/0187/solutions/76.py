class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        curr=0
        rounds=0
        maximum=0
        ans=-1
        profit=0
        for i in customers:
            curr+=i
            #print(curr)
            if curr>=4:
                profit+=boardingCost*4-runningCost
                rounds+=1
                curr-=4
            else:
                rounds+=1
                profit+=boardingCost*curr-runningCost
                curr=0
            if profit>maximum:
                ans=rounds
                maximum=profit
        while curr>0:
            if curr>=4:
                profit+=boardingCost*4-runningCost
                rounds+=1
                curr-=4
            else:
                #print('here')
                rounds+=1
                profit+=boardingCost*curr-runningCost
                curr=0
            if profit>maximum:
                ans=rounds
                maximum=profit
            #print(curr,profit)
        return ans
