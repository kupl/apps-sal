class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {0: (4,6), 1: (8, 6), 2: (7, 9), 3: (4, 8), 4: (0, 3, 9), 6: (0, 1, 7), 7: (2, 6), 8: (1,3), 9: (2, 4)}
        @lru_cache(None)
        def dfs(last_val=None, length=0):
            if length == n:
                return 1
            count = 0
            if not length:
                for i in range(0,10): 
                    count += dfs(i, 1)
            elif last_val != 5:
                for i in moves[last_val]:
                    count += dfs(i, length+1)
            return count
        return dfs() % ((10**9)+7)
                
        

