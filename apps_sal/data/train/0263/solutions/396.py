class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9+7
        c = [1]*10
        for _ in range(n-1):
            c = [
                c[4]+c[6], c[6]+c[8],
                c[7]+c[9], c[4]+c[8],
                c[0]+c[3]+c[9], 0,
                c[0]+c[7]+c[1], c[2]+c[6],
                c[1]+c[3], c[2]+c[4]
            ]
        return sum(c)%mod
