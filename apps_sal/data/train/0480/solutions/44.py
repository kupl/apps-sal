class Solution:
    def numWays(self, s: int, a: int) -> int:
        MOD = 1000000007
        mem = {}
        def f(s, a, i):
            if (s, i) in mem:
                return mem[(s,i)]
            if not s:
                if i:
                    return 0
                return 1
            if i < 0 or i == a:
                return 0
            #if i > s:
            #    return 0
            ans = 0
            #stay
            ans += f(s-1, a, i)
            #left
            ans += f(s-1, a, i-1)
            #right
            ans += f(s-1, a, i+1)
            
            mem[(s,i)] = ans
            return ans%MOD
            
        return f(s, a, 0)
            
            
        
            
    

