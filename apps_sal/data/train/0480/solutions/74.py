class Solution:

    def helper(self, pos, steps):
        if (pos, steps) in self.cache:
            return self.cache[pos, steps]
        if steps == 0:
            return 1 if pos == 0 else 0
        stay = self.helper(pos, steps - 1)
        self.cache[pos, steps - 1] = stay
        left = self.helper(pos + 1, steps - 1) if pos < self.arrLen - 1 else 0
        self.cache[pos + 1, steps - 1] = left
        right = self.helper(pos - 1, steps - 1) if pos > 0 else 0
        self.cache[pos - 1, steps - 1] = right
        return stay + left + right

    def numWays(self, steps: int, arrLen: int) -> int:
        self.cache = {}
        self.steps = steps
        self.arrLen = arrLen
        return self.helper(0, steps) % (10 ** 9 + 7)
