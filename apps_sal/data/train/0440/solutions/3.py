class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(p, q):
            while q > 0:
                p, q = q, p % q 
            return p
            
        lcm = p * q // gcd(p, q)
        if (lcm // q) % 2 == 0:
            return 2
        elif (lcm // p) % 2 == 1:
            return 1
        else:
            return 0
