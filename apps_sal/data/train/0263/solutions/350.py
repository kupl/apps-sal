class Solution:
    NEIGHBORS = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: (), 6: (1, 7, 0), 7: (2, 6), 8: (1, 3), 9: (2, 4)}

    def numsFromPos(self, num, jumps):
        jumps_remaining = jumps - 1
        if not jumps_remaining:
            return 1
        if (num, jumps) in self.cache:
            return self.cache[num, jumps]
        res = 0
        for nei in self.NEIGHBORS[num]:
            res += self.numsFromPos(nei, jumps_remaining)
        self.cache[num, jumps] = res
        return res

    def knightDialer(self, n: int) -> int:
        self.cache = {}
        res = 0
        for i in range(10):
            res += self.numsFromPos(i, n)
        return res % (10 ** 9 + 7)
