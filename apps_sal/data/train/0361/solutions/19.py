class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        dp = [[sys.maxsize]*(m+1) for _ in range(n+1)]
        
        def getdp(n, m):
            if dp[n][m] != sys.maxsize: return dp[n][m]
            if n == 0 or m == 0: return 0
            
            # base cases
            if m == n: return 1
            if m == 1: return n
            if n == 1: return m
            
            # otherwise we break up the whole chunk
            ans = n*m
            
            # horizontal cut
            for i in range(1, n//2+1):
                ans = min(ans, getdp(i, m) + getdp(n-i, m))
            
            # vertical cut
            for i in range(1, m//2+1):
                ans = min(ans, getdp(n, i) + getdp(n, m-i))
            
            # leave out the center
            for l in range(1, min(n,m)-2):
                for i in range(2, n+1-l):
                    for j in range(2, m+1-l):
                        ans = min(ans, getdp(i+l-1, j-1) + getdp(i-1, m-j+1) + getdp(n-(i+l-1), j+l-1) + getdp(n-i+1, m-(j+l-1))+1)
            dp[n][m] = ans
            return ans

        return getdp(n, m)
