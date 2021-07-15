from functools import lru_cache

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.n = sum(balls) // 2
        self.balls = balls
        return self.dfs(0, 0, 0, 0, 0)
        
    def com(self, n, m):
        ans = 1
        for i in range(n-m+1, n+1):
            ans *= i
        for i in range(1, m+1):
            ans //= i
        return ans
        
    @lru_cache(None)
    def dfs(self, left, right, i, ul, ur):
        if i == len(self.balls):
            return float(ul == ur)
        p = 0
        for l in range(self.balls[i]+1):
            r = self.balls[i] - l
            if left+l > self.n or r+right > self.n:
                continue
            p += self.com(self.n-left, l) * self.com(self.n-right, r) / self.com(2*self.n-left-right, self.balls[i]) * self.dfs(left+l, right+r, i+1, ul+(l>0), ur+(r>0))
        return p
