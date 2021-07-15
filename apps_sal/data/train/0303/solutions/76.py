class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
         
        best_a = [0] * len(A)
        best_a[0] = A[0]
       
        for i in range(1, len(A)):
            max_v = 0
            for j in range(i, max(-1, i-K), -1):
                sa = A[j:i+1]
                v = best_a[j-1] + max(sa) * len(sa)
                if v > max_v:
                    max_v = v
                #print(best_a,max_v,i,j,sa)
            best_a[i] = max_v
        
        return best_a[-1]
        
        
        

