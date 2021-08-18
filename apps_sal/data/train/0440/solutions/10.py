class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0:
            return 0
        div = gcd(p, q)
        h, v = p // div, q // div
        if not h % 2:
            return 2
        if v % 2:
            return 1
        return 0
