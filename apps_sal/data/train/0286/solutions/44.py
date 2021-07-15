class Solution(object):
    def __init__(self):
        self.fact = [1, 1, 2, 6, 24, 120, 720]
        self.total = 0.0
        self.match = 0.0

    def dfs(self, balls, i=0, n=0, c=0, w=1.0):
        if i == len(balls):
            self.total += w * (n == 0)
            self.match += w * (n == 0) * (c == 0)
            return
        for b1, b2 in zip(range(balls[i] + 1), reversed(range(balls[i] + 1))):
            self.dfs(
                balls,
                i + 1,
                n + b1 - b2,
                c + (b2 == 0) - (b1 == 0),
                w / self.fact[b1] / self.fact[b2])

    def getProbability(self, balls):
        self.dfs(balls)
        return self.match / self.total
