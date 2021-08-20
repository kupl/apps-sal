class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        self.mod = 1000000000.0 + 7
        self.cache = {}
        self.knight_steps = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        count = 0
        for i in range(10):
            count += self.recursive_calc(i, n - 1)
            count = count % self.mod
        return int(count % self.mod)

    def recursive_calc(self, current_number, steps):
        if steps == 0:
            return 1
        if (current_number, steps) in self.cache:
            return self.cache[current_number, steps]
        total = 0
        for i in self.knight_steps[current_number]:
            total += self.recursive_calc(i, steps - 1)
            total = total % self.mod
        self.cache[current_number, steps] = total
        return self.cache[current_number, steps]
