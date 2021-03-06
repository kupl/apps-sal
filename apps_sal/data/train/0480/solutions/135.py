class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        memory = {}

        def helper(i, steps):
            if i < 0 or i == arrLen:
                return 0
            if i > steps:
                return 0
            if i == steps:
                return 1
            prev = memory.get((i, steps))
            if prev is not None:
                return prev
            steps -= 1
            stay = helper(i, steps)
            left = helper(i - 1, steps)
            right = helper(i + 1, steps)
            memory[i, steps + 1] = stay + left + right
            return memory[i, steps + 1]
        return helper(0, steps) % MOD
