class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        result = 2
        
        L = len(A)
        index = [-1] * 2001 
        
        dp = [[2] * L for _ in range(L)]

        
        for i in range(L - 1):
            for j in range(i + 1, L):
                prevVal = 2 * A[i] - A[j]
                
                if index[prevVal] == -1:
                    continue
                else:
                    idx = index[prevVal]
                    if idx == -1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[idx][i] + 1
                        result = max(result, dp[i][j])
            
            index[A[i]] = i
        
        return result
