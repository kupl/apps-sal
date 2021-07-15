class Solution:
    
    def palindromePartition(self, S: str, K: int) -> int:
        
        def palindrome_distance(li, ri):
            count = 0

            while li < ri:
                count += S[li] != S[ri]
                li += 1
                ri -= 1
                
            return count
        
        def dfs(i, k):
            if i == N or k == 0:
                return 0 if i == N and k == 0 else math.inf
            
            if (i, k) in memo:
                return memo[i, k]
            
            ans = math.inf
            
            for j in range(i, N):
                if (i, j) not in dist_memo:
                    dist_memo[i, j] = palindrome_distance(i, j)
                
                val = dist_memo[i, j] + dfs(j+1, k-1)
                ans = min(ans, val)
                
            memo[i, k] = ans
            return ans
                
        
        N = len(S)
        memo = {}
        dist_memo = {}
        ans = dfs(0, K)
        return ans

