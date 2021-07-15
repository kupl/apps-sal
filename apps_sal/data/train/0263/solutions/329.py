class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        MOD = 10**9 + 7
        res = 0
        cache = {}
        for i in range(10):
            res += self.helper(i,n,neighbors,cache)
        return res % MOD
    def helper(self,num,hops,neighbors,cache):
        if hops == 1:
            return 1
        if (num,hops) in cache:
            return cache[(num,hops)]
        seq = 0
        for i in neighbors[num]:
            seq += self.helper(i,hops-1,neighbors,cache)
        cache[(num,hops)] = seq
        return seq
