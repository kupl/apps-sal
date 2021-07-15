class Solution:
    def knightDialer(self, n: int) -> int:
        # mp = {0: [4,6], 1: [6, 8], 2: [9,7], 3: [8,4], 4:[9, 0, 3], 5:[], 6: [1, 7, 0], 7: [6, 2], 8:[3,1], 9: [2,4]}
        c = 0
        mp = [[4,6], [6,8], [9,7], [8,4], [0,9,3], [],[1,7,0],[6,2],[3,1], [2,4]]
        memo = {}
        for i in range(0, 10):
            c += self.gen(i, n, mp, memo)
        mpow = (10**9) + 7
        return c % mpow
    
    def gen(self, start, n, mp, memo):
        if n == 1:
            return 1
        key = (start, n)
        if key in memo:
            return memo[key]
        c = 0
        for opt in mp[start]:
            c += self.gen(opt, n-1, mp, memo)
        memo[key] = c
        return c
        
            

