class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)  # 总球数
        k = len(balls)  # 球色数
        self.total = self.valid = 0
        fact = [1] * 50  # 得到每个数的阶乘
        for i in range(1, 50):
            fact[i] = fact[i - 1] * i
        #d: depth
        # b1, b2: # of balls in box1, box2
        # c1,c2 :两个box中不同色的球数
        # p1, p2: # permutations of duplicate balls in box1, box2

        def dfs(d, b1, b2, c1, c2, p1, p2):
            if b1 > n // 2 or b2 > n // 2:
                return
            if d == k:
                count = fact[b1] / p1 * fact[b2] / p2
                self.total += count
                self.valid += count * (c1 == c2)
                return
            for s1 in range(balls[d] + 1):
                s2 = balls[d] - s1
                dfs(d + 1, b1 + s1, b2 + s2, c1 + (s1 > 0), c2 + (s2 > 0), p1 * fact[s1], p2 * fact[s2])
        dfs(0, 0, 0, 0, 0, 1, 1)
        return self.valid / self.total
