class Solution:
    @lru_cache(maxsize=None)
    def startFrom(self, i, l):
        if l <= 1:
            return 1 if l == 1 else 0
        else:
            return sum([self.startFrom(j, l - 1) for j in self.mapping[i]]) % (10**9 + 7)

    def knightDialer(self, n: int) -> int:
        self.mapping = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        return sum([self.startFrom(i, n) for i in range(10)]) % (10**9 + 7)
