# class Solution:
#    def superEggDrop(self, K: int, N: int) -> int:
#        def solve(e,f,dp):
#            if f==0:
#                return f
#            elif e==1:
#                return f
#
#            if dp[e][f]!=-1:
#                return dp[e][f]
#            l,h=1,f
#            while l+1<h:
#                x=(l+h)//2
#                if dp[e][f-x]!=-1:
#                    f1=dp[e][f-x]
#                else:
#                    f1=solve(e,f-x,dp)
#                if dp[e-1][x-1]!=-1:
#                    f2=dp[e-1][x-1]
#                else:
#                    f2=solve(e-1,x-1,dp)
#                if f1<f2:
#                    l=x
#                elif f2>f1:
#                    h=x
#                else:
#                    l=h=x
#
#            ans=1+min(max(solve(e,f-x,dp),solve(e,x-1,dp)) for x in range(l,h+1))
#            dp[e][f]=ans
#            return dp[e][f]
#        dp=[[-1]*(N+1) for i in range(K+1)]
#        return solve(K,N,dp)
class Solution(object):
    def superEggDrop(self, K, N):
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    ans = 1000000
                    for x in range(lo, hi + 1):
                        temp = 1 + max(dp(k - 1, x - 1), dp(k, n - x))
                        if ans > temp:
                            ans = temp

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)
