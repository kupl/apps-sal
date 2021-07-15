class Solution:
    def minOperationsMaxProfit(self, A, BC, RC):
        ans=profit=t=0
        maxprofit=0
        wait=i=0
        n=len(A)
        while wait or i<n:
            if i<n:
                wait+=A[i]
                i+=1
            t+=1
            y=wait if wait<4 else 4
            wait-=y
            profit+=y*BC
            profit-=RC
            if profit>maxprofit:
                maxprofit=profit
                ans=t
        
        profit+=wait//4*BC + wait%4*BC
        rot=(wait+3)//4
        profit-=RC*rot
        if profit>maxprofit:
            ans+=rot

        if maxprofit<=0:
            return -1
        else:
            return ans

