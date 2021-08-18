class Solution:

    def knightDialer(self, k: int) -> int:
        self.dirs = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1]
        ]

        self.mod = 10 ** 9 + 7

        self.n = 4
        self.m = 3
        if k == 1:
            return 10

        self.forbidden = set([(3, 0), (3, 2)])
        self.next_pos = self.build_pos()
        self.dp = [1] * 10
        self.helper(k - 1)
        return sum(self.dp) % self.mod

    def helper(self, k):
        if k == 0:
            return
        next_dp = [0] * 10
        for i in range(10):
            for j in self.next_pos[i]:
                next_dp[j] += (self.dp[i] % self.mod)
                next_dp[j] %= self.mod
        self.dp = next_dp
        self.helper(k - 1)

    def build_pos(self):
        res = {}
        for i in range(10):
            next_num = []
            x, y = self.get_pos(i)
            for d in self.dirs:
                nx, ny = d
                if self.is_valid(x + nx, y + ny):

                    num = self.get_num(x + nx, y + ny)
                    next_num.append(num)
            res[i] = next_num
        return res

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and (x, y) not in self.forbidden

    def get_num(self, x, y):
        if x == 3 and y == 1:
            return 0
        if self.is_valid(x, y):
            return x * 3 + y + 1

    def get_pos(self, num):
        if num == 0:
            return (3, 1)
        num -= 1
        row = num // 3
        col = num % 3
        return (row, col)
