class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = 10**9 + 7
        self.count = 0
        self.cache = {}

        for digit in range(0, 10):
            self.count += self.getWays(digit, n - 1)

        return self.count % modulo

    def getWays(self, digit, n):
        if n == 0:
            return 1

        if (digit, n) in self.cache:
            return self.cache[(digit, n)]

        temp = 0
        for neighbor in self.neighbors(digit):
            temp += self.getWays(neighbor, n - 1)

        self.cache[(digit, n)] = temp
        return self.cache[(digit, n)]

    def neighbors(self, digit):
        neighbors = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)

        }

        return neighbors[digit]
