class Solution:

    def isGoodArray(self, x: List[int]) -> bool:
        g = x[0]
        for i in x:
            g = gcd(i, g)
        return g == 1
