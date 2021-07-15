class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans=0
        
        cust=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                cust+=customers[i]
                customers[i]=0
        
        cur=0
        best=0
        
        for i,c in enumerate(customers):
            cur+=c
            if i>=X:
                cur-=customers[i-X]
            best=max(best,cur)
        return cust+best
            

