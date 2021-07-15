class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        #if not A: return 0
        #if len(A)==1: return A[0]
        # Real Run Time is a little bit UNSTABLE
        N = len(A)
        P = [0] * (N+1)
        for i in range(1,N+1): P[i] = P[i-1] + A[i-1] # 注： cumulative sum of A[:i]
        
        # Table[a] = optimal for A[a:] with k subsets, initially k=1
        Table = [(P[N]-P[i])/(N-i) for i in range(N)]
        for k in range(2, K+1): # 注： starting from k=2 subsets, end at k=K subsets at most
            # 注： optimal for A[i:] with k subsets means: optimal pair{ 1 subset A[i:j] and optimal A[j:] with (k-1) subsets whose value saved in Table[j], where i+1=<j<=N-(k-1)}
            for i in range(K-k,N-(k-1)): # 注： 
                Table[i] = max((P[j]-P[i])/(j-i) + Table[j] for j in range(i+1,N-(k-1)+1))
        
        return Table[0]   
