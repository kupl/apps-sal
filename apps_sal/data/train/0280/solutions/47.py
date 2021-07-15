class Solution1:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = [[0] * len(s) for i in range(len(s))]
        
        n = len(s)
        
        def transferPalimCount(s) -> int:
            res = 0
            q = len(s) - 1
            p = 0
            
            while p < q:
                if s[p] != s[q]:
                    res += 1
                p += 1
                q -= 1
            return res

        for i in range(n):
            for j in range(i, n):
                dp[i][j] = transferPalimCount(s[i:j+1])
                
                

        def findMin(s, e, k, count, candidates):
            if k == 0:
                if s > e:
                    candidates.append(count)
                    return
                else:
                    count += dp[s][e]
                    candidates.append(count)
                    return
            
            # string is not able to split to too much parts
            if e-s+1 < k+1:
                return
        
            for i in range(s, e+1):
                findMin(i+1, e, k-1, count + dp[s][i], candidates)

        candidates = []
        findMin(0, n-1, k-1, 0, candidates)
        
        return min(candidates)

# https://leetcode.com/problems/palindrome-partitioning-iii/discuss/441427/Python3-Top-down-DFS-with-Memoization
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        def cost(s,i,j):
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r
        
        def dfs(i, k):
            # case already in memo
            if (i, k) in memo: return memo[(i, k)]
            
            if n - i < k:
                return float('inf')
            
            # base case that each substring just have one character
            if n - i == k:
                return 0
            
            # base case that need to transfer whole substring into palidrome
            if k == 1:
                return cost(s, i, n - 1)

            res = float('inf')

            # keep making next part of substring into palidrome
            for j in range(i + 1, n):

                # compare different divisions to get the minimum cost
                res = min(res, dfs(j, k - 1) + cost(s, i, j - 1))
            memo[(i, k)] = res
            return res
        return dfs(0 , k)
        
        
        
                    

