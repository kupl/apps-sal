class Solution:
    def __init__(self):
        self.memo = {0: False}
        
    def winnerSquareGame(self, n: int) -> bool:
        def rwsg(n,picks):
            if n not in self.memo:
                out = False
                for p in picks:
                    if p > n: break
                    out = out or not rwsg(n-p,picks)
                self.memo[n] = out
            return self.memo[n]
        picks = []
        m = 1
        while m*m <= n:
            picks.append(m*m)
            m += 1
        rwsg(n,picks)
        return rwsg(n,picks)
