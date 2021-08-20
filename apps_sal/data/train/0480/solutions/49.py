class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}

        def helper(position, num_steps, idx):
            nonlocal steps, arrLen, memo
            if (position, num_steps, idx) in memo:
                return memo[position, num_steps, idx]
            if idx < 0 or idx > arrLen - 1:
                return 0
            if num_steps == steps:
                if position == 0:
                    return 1
                return 0
            stay = helper(position, num_steps + 1, idx)
            right = helper(position + 1, num_steps + 1, idx + 1)
            left = helper(position - 1, num_steps + 1, idx - 1)
            memo[position, num_steps, idx] = stay + left + right
            return memo[position, num_steps, idx]
        return helper(0, 0, 0) % (10 ** 9 + 7)
