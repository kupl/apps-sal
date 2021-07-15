class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        # [# of 0, # of 4/6, # of 2/8, # of corners]
        a,b,c,d = [1,2,2,4]
        for i in range(n-1):
            a,b,c,d = [b, 2*a+d, d, 2*(b+c)]
        return sum([a,b,c,d]) % (10**9 + 7)
