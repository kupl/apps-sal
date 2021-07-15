class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == 1 or b == 1:
            return 1
        while b != 0:
            a, b = b, a % b
        return a
    
    def isGoodArray(self, nums: List[int]) -> bool:
        g = 0
        for n in nums:
            if g == 0:
                g = n
            elif n == 1:
                return True
            else:
                while n:
                    g, n = n, g % n
            if g == 1:
                return True
        return False
