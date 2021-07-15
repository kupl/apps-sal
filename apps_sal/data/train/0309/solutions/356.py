class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = {}
        dp = {i:defaultdict(int) for i in range(len(A))}
        mx = 0
        
        for i in range(len(A)):
            if A[i] not in d: d[A[i]] = 1

            for j in range(0, i):
                ap = A[i] + -A[j]
            
            
                if A[i] + -ap in d:
                    dp[i][ap] = dp[j][ap] + 1
                    mx = max(mx, dp[i][ap])
                    
        return mx+1 
