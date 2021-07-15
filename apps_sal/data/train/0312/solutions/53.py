class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # make p array which is a cumulative sum
        p=[0]
        
        for i in range(len(A)):
            p.append(p[-1]+A[i])
            
        q=[]
        result=len(A)+1 # a high value
        for i in range(len(A)+1):
            
            while(q and p[i]-p[q[0]]>=K):
                result = min( result , i-q[0])
                q.pop(0)
                
            while(q and p[i]-p[q[-1]]<=0):
                q.pop()
            
            q.append(i)
            
        return(-1 if result==len(A)+1 else result)
            

