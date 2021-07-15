class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:        
        lo = 1
        hi = 2*10**9;
        
        ab = a * b // math.gcd(a, b);
        bc = b * c // math.gcd(b, c);
        ac = a * c // math.gcd(a, c);
        abc = a * bc // math.gcd(a, bc);
        
        while lo < hi:
            mid = lo + (hi - lo)//2;
            cnt = mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ac + mid//abc;
            if cnt < n: 
                lo = mid + 1;
            else:
                hi = mid;
        
        return lo
