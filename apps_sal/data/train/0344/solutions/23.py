class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        def compare(i, j):
            return all(A[k][i] <= A[k][j] for k in range(len(A)))
        
        l = len(A[0])
        dp = [1 for _ in range(l)] + [0]
        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1, l):
                if compare(i, j):
                    dp[i] = max(dp[i], dp[j]+1)
        
        
        return l - max(dp[i] for i in range(l))
