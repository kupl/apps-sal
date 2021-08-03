class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] + list(accumulate(nums))
        len_dp = len(dp)
        answer = 0
        lo = 0
        lo_sum = 0
        for hi in range(1, len_dp):
            if dp[hi] < lo_sum:
                lo_sum = dp[hi]
            if dp[hi] - lo_sum >= target:
                if dp[hi] - target in dp[lo:hi]:
                    answer += 1
                    lo = hi
                    lo_sum = dp[hi]
        return answer
