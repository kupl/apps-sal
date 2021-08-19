class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        def count_steps(steps_left, current_pos, memo):
            if (steps_left, current_pos) in memo:
                return memo[steps_left, current_pos]
            if current_pos < 0 or current_pos > arrLen - 1 or current_pos > steps_left:
                return 0
            if not steps_left:
                if current_pos == 0:
                    return 1
                else:
                    return 0
            ans = count_steps(steps_left - 1, current_pos, memo) + count_steps(steps_left - 1, current_pos - 1, memo) + count_steps(steps_left - 1, current_pos + 1, memo)
            memo[steps_left, current_pos] = ans % MOD
            return memo[steps_left, current_pos]
        return count_steps(steps, 0, {})
