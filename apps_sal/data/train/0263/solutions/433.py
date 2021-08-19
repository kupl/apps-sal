class Solution:

    def __init__(self):
        self.memory = {}

    def knightDialer(self, n: int) -> int:
        steps = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 9, 3], 5: [], 6: [7, 1, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        def kDialer(i, n, steps, c):
            if n == 1:
                return 1
            if n == 0:
                return 0
            if (i, n) in self.memory:
                return self.memory[i, n]
            self.memory[i, n] = 0
            for j in steps[i]:
                self.memory[i, n] += kDialer(j, n - 1, steps, c) % c
            self.memory[i, n] = self.memory[i, n] % c
            return self.memory[i, n]
        combinations = 0
        for i in range(0, 10):
            combinations += kDialer(i, n, steps, 10 ** 9 + 7) % (10 ** 9 + 7)
        return combinations % (10 ** 9 + 7)
