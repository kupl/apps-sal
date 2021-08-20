class Solution:

    def __init__(self):
        self.memo = {}

    def getOrCreate(self, i, n):
        if (i, n) not in self.memo:
            self.memo[i, n] = self.__knightDialerDP(i, n)
        return self.memo[i, n]

    def __knightDialerDP(self, i, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if i == 0:
            return self.getOrCreate(4, n - 1) + self.getOrCreate(6, n - 1)
        elif i == 1:
            return self.getOrCreate(6, n - 1) + self.getOrCreate(8, n - 1)
        elif i == 2:
            return self.getOrCreate(7, n - 1) + self.getOrCreate(9, n - 1)
        elif i == 3:
            return self.getOrCreate(4, n - 1) + self.getOrCreate(8, n - 1)
        elif i == 4:
            return self.getOrCreate(0, n - 1) + self.getOrCreate(3, n - 1) + self.getOrCreate(9, n - 1)
        elif i == 6:
            return self.getOrCreate(0, n - 1) + self.getOrCreate(1, n - 1) + self.getOrCreate(7, n - 1)
        elif i == 7:
            return self.getOrCreate(2, n - 1) + self.getOrCreate(6, n - 1)
        elif i == 8:
            return self.getOrCreate(1, n - 1) + self.getOrCreate(3, n - 1)
        elif i == 9:
            return self.getOrCreate(2, n - 1) + self.getOrCreate(4, n - 1)
        else:
            return 0

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return 0
        for k in range(n):
            total_count = 0
            for i in range(10):
                total_count += self.__knightDialerDP(i, k + 1)
        return total_count % (10 ** 9 + 7)
