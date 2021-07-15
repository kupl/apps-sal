class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [[0 for _ in range(len(A))] for _ in range(2)]
        
        dp2 = [0 for _ in range(len(A))]
        
        for i in range(len(A)):
            # we have 2 options - to partition or not to partition.
            
#             if i - K + 1 < 0:
#                 maxCand = max(A[:i+1])
#                 size = i + 1
#             else:
#                 maxCand = max(A[i - K + 1:i+1])
#                 size = K
                
#             # if we choose not to partition
#             dp[0][i] = size * maxCand + max(dp[0][i - K], dp[1][i - K])
            
#             # if we choose to partition at this candidate
#             dp[1][i] = A[i] + max(dp[0][i - 1], dp[1][i - 1])

            startIndex = max(0, i - K + 1)
    
            while startIndex <= i:
                if startIndex - 1 >= 0:
                    dp2[i] = max(dp2[startIndex - 1] + max(A[startIndex:i+1])*(i + 1 - startIndex), dp2[i])
                else:
                    dp2[i] = max(A[:i+1]) * (i + 1)
                    
                startIndex += 1
                    
        print(dp2)   
        return dp2[-1]
