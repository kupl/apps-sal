class Solution:
    s = [0]

    def findKthBit(self, n: int, k: int) -> str:
        while len(self.s) < k:
            self.s = self.s + [1] + [n ^ 1 for n in self.s[::-1]]

        return str(self.s[k - 1])
