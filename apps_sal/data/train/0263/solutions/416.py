class Solution:
    def knightDialer(self, N: int) -> int:
        choices = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        self.memo = dict()
        
        def dfs(curr, n):
            key = (curr, n)
            if key in self.memo:
                return self.memo[key]
            
            if n == 1:
                return 1
            
            sub = 0
            for next in choices[curr]:
                sub += dfs(next, n - 1)
            
            self.memo[key] = sub
            return sub
        
        res = 0
        for s in range(10):
            res += dfs(s, N)
                
        return res % (10 ** 9 + 7)

