from functools import lru_cache
class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def jumps(start, n):
            if n == 0:
                return 1
            ans = 0
            for neighbor in neighbors[start]:
                ans = (ans + jumps(neighbor, n-1)) % MOD
            return ans % MOD
        
        neighbors = {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            5: [],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4],
            0: [4,6]
        }
        MOD = pow(10, 9) + 7
        res = 0
        for i in range(10):
            res = (res + jumps(i, n-1)) % MOD
        return res
