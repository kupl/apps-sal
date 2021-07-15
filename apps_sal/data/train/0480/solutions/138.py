class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        const = 10**9+7
        def num(step, idx) -> int:
            if (step, idx) in memo:
                return memo[(step, idx)]
            if idx < 0 or idx >= arrLen:
                return 0
            if step <= 0:
                return idx == step
            if idx > step:
                return 0
            elif idx == step:
                return 1
            else:
                memo[(step, idx)] = num(step-1, idx) + num(step-1, idx-1) + num(step-1, idx+1)  
                if memo[(step, idx)] > const:
                    memo[(step, idx)] = memo[(step, idx)]%const
                return memo[(step, idx)]
        return num(steps, 0)
