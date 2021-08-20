class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        last_dp = [1] * 10
        this_dp = [0] * 10
        next_steps = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        for _ in range(2, n + 1):
            for i in range(10):
                if i != 5:
                    this_dp[i] = sum((last_dp[next_step] for next_step in next_steps[i])) % int(10 ** 9 + 7)
            last_dp = this_dp
            this_dp = [0] * 10
        return sum(last_dp) % int(10 ** 9 + 7)
