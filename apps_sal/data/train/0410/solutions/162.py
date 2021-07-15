class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        
        ans=[]
        for x in range(lo,hi+1):
            count=0
            num=x
            while x>1:

                if x%2==0:
                    x=x/2
                else:
                    x=3*x+1
                count+=1
            heapq.heappush(ans,[count,num])
        
     
        return (heapq.nsmallest(k,ans)[-1][-1])
    

