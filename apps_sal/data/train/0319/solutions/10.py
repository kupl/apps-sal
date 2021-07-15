from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + stoneValue[i]
            
        @lru_cache(None)
        def dp(start: int) -> int:
            if start >= n:
                return 0
            min_next = 2 ** 30
            for i in range(1, 4):
                min_next = min(min_next, dp(start + i))
            return psum[n] - psum[start] - min_next
        
        alice = dp(0)
        bob = psum[n] - alice
        return 'Alice' if alice > bob else 'Bob' if bob > alice else 'Tie'
