class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @lru_cache(None)
        def helper(i,t):
            if(i>=len(A)):
                return 0
            if(t==K-1):
                return sum(A[i:])/(len(A)-i)
            else:
                m=-1
                for j in range(1,len(A)-i):
                    m=max(m,helper(i+j,t+1)+sum(A[i:i+j])/j) 
                return m
        return helper(0,0)
