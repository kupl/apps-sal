class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        return self.dfs(steps, arrLen, {}, 0) % (10 ** 9 + 7)

    def dfs(self, step, arrLen, mem, index):
        if (step, index) in mem:
            return mem[step, index]
        if index < 0 or index >= arrLen:
            return 0
        if step == 0:
            if index == 0:
                return 1
            return 0
        mem[step, index] = 0
        for i in range(-1, 2):
            mem[step, index] += self.dfs(step - 1, arrLen, mem, index + i)
        return mem[step, index]
