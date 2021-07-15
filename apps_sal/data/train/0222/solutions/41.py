class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2] * n for i in range(n)]
        
        m = dict()
        for i in range(n):
            m[A[i]] = i
            
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                a_k = A[j] - A[i]
                if a_k > A[i]:
                    break
                k = m.get(a_k, None)
                if k is not None and k < i:
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])
        return ans if ans >= 3 else 0
                
                

