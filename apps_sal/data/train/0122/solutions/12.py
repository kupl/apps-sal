class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        # prefix sum solution
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i] + cardPoints[i]
            
        max_val = -1
        
        for i in range(k+1):
            max_val = max(max_val, pre[i] + pre[n] - pre[n-k+i])
            
        return max_val
        
#         if k >= n:
#             return sum(cardPoints)
        
#         def dfs(i,j):
#             if i + (n-j-1) >= k:
#                 return 0
            
#             else:
#                 return max(dfs(i+1,j)+cardPoints[i], dfs(i,j-1)+cardPoints[j])
            
#         return dfs(0,n-1)

