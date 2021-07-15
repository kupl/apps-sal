
class Solution:
    import sys
    
    def countOrders(self, n: int) -> int:
        
        print(sys.getrecursionlimit())
        #A = [0 for _ in range(n)]
        
        @lru_cache(None)
        def helper(p,d):
            #sys.setrecursionlimit(10**6)
            if(p == n and d == n):
                return 1
            ans = 0
            if(n>p):
                ans += (n-p)*(helper(p+1,d))
            if(p>d):
                ans += (p-d)*(helper(p,d+1))
            return ans
        
        return helper(0,0)%(10**9 + 7)
