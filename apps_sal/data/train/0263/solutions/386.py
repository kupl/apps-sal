class Solution:
    def knightDialer(self, N: int) -> int:
        
        g = {0:[4,6],
             1:[6,8],
             2:[7,9],
             3:[4,8],
             4:[3,9,0],
             5:[],
             6:[1,7,0],
             7:[2,6],
             8:[1,3],
             9:[4,2]}
        
        A = [[1 if i in g[j] else 0 for i in range(10)] for j in range(10)]
        
        v = [1]*10
        for _ in range(N-1):
            res = [0]*10
            for r in range(10):
                for c in range(10):
                    if A[r][c]:
                        res[c] += v[r]
            v = res
        return sum(v) % (10**9 + 7)
