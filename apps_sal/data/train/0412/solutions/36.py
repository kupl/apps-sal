class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # bottom up DP
        prev_dp = [0] * (target + 1)
        prev_dp[0] = 1
        for num_dice in range(1, d + 1):
            curr_dp = [0] * (target + 1)
            for face in range(1, f+1):
                for total in range(face, target + 1):
                    curr_dp[total] = (curr_dp[total] + prev_dp[total - face]) % (10 ** 9 + 7)
            prev_dp = curr_dp
        return prev_dp[-1]
