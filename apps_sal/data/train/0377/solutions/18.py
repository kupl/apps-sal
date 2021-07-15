from fractions import gcd
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        l = 0
        r = N*(min(A, B))
        
        lcm = (A*B)//gcd(A, B)
        
        def checkNum(x):
            ans = x//A + x//B - x//lcm
            return ans >= N
        
        if N == 1:
            return min(A, B)
        while r > l:
            m = (r + l) // 2
            if checkNum(m):
                r = m
            else:
                l = m + 1
        return l%(10**9+7)
