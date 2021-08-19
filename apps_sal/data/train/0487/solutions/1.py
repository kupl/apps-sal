class Solution:

    def longestDiverseString(self, a: int, b: int, c: int, charA='a', charB='b', charC='c') -> str:
        if a < b:
            return self.longestDiverseString(b, a, c, charB, charA, charC)
        if b < c:
            return self.longestDiverseString(a, c, b, charA, charC, charB)
        if b == 0:
            return min(a, 2) * charA
        use_a = min(2, a)
        use_b = 1 if a - use_a >= b else 0
        return charA * use_a + charB * use_b + self.longestDiverseString(a - use_a, b - use_b, c, charA, charB, charC)
