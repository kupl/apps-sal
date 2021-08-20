class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        self.dic = dict()
        self.search(steps, arrLen, 0)
        return self.search(steps, arrLen, 0) % (10 ** 9 + 7)

    def search(self, steps, arrLen, start):
        if (steps, start) in self.dic:
            return self.dic[steps, start]
        if start > steps:
            return 0
        if start == 0 and steps == 0:
            return 1
        output = 0
        output += self.search(steps - 1, arrLen, start)
        if start > 0:
            output += self.search(steps - 1, arrLen, start - 1)
        if start < arrLen - 1:
            output += self.search(steps - 1, arrLen, start + 1)
        self.dic[steps, start] = output
        return output
