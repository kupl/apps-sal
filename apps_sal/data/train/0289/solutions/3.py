class Solution:
    def maxSumTwoNoOverlap(self, arr: List[int], L: int, M: int) -> int:
        
        n=len(arr)
        pre=[arr[0] for i in range(len(arr))]
        for j in range(1,n):
            pre[j]=pre[j-1]+arr[j]
            
        res1=-1   
        for i in range(n-(L+M)+1):
            for k in range(i+L,n-M+1):
                sum1=pre[i+L-1]-(pre[i-1] if i>0 else 0)
                sum2=pre[k+M-1]-(pre[k-1] if k>0 else 0)
                res1=max(res1,sum1+sum2)       
        res2=-1       
        for i in range(n-(L+M)+1):
            for k in range(i+M,n-L+1):
                sum1=pre[i+M-1]-(pre[i-1] if i>0 else 0)
                sum2=pre[k+L-1]-pre[k-1]
                res2=max(res2,sum1+sum2)
                
        return max(res1,res2)
