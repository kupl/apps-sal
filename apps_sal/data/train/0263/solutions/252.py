class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 = 1,1,1,1,1,0,1,1,1,1
        for i in range(1, n):
            x0,x1,x2,x3,x4,x6,x7,x8,x9 = x4+x6,x6+x8,x7+x9,x4+x8,x0+x3+x9,x0+x1+x7,x2+x6,x1+x3,x2+x4
        return (x1+x2+x3+x4+x5+x6+x7+x8+x9+x0)%(10**9+7)
