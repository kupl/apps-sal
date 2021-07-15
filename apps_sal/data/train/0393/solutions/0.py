class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def enough(num):
            total = num//a + num//b + num//c -num//ab - num//bc - num//ac + num//abc
            return total>=n
    
    
        ab = (a*b)//math.gcd(a,b)
        ac = (a*c)//math.gcd(a,c)
        bc = (b*c)//math.gcd(b,c)
        abc = (a*bc)//math.gcd(a,bc)
        
        
        left , right = 1, min(a,b,c)*n
        
        while left < right:
            mid = left+ (right-left)//2
            if enough(mid): right = mid
            else : left = mid + 1
                
        return left
