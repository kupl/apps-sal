class Solution:
    
    BASE = 10 ** 9 + 7
    
    def knightDialer(self, N: int) -> int:
        if N <= 1:
            return 10
        a, b, c, d = 2, 4, 2, 1
        for _ in range(N - 1):
            a, b, c, d = (b, 2 * (a + c) % self.BASE, (b + 2 * d) % self.BASE, c)
        return (a + b + c + d) % self.BASE
