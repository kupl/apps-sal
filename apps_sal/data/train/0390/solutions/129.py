class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.memo = {}
        return self.helper(n)
    
    def helper(self, n):
        if n == 0:
            return False
        if n in self.memo:
            return self.memo[n]
        i = 1
        while i * i <= n:
            if not self.helper(n - i * i):
                self.memo[n] = True
                return True
            i += 1
        self.memo[n] = False
        return False

