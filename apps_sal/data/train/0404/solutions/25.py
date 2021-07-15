class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        mem = {}
        def dfs(l, K):
            if((l, K) in mem):
                return mem[(l, K)]
            if(l==len(A)):
                return 0
            if(K==1):
                return(sum(A[l:])/len(A[l:]))
            ans = sum(A[l:])/len(A[l:])
            for i in range(l+1, len(A)):
                avg = sum(A[l:i])/len(A[l:i])
                ans = max(ans, avg+dfs(i, K-1))
            mem[(l, K)]=ans
            return ans
        return dfs(0, K)
