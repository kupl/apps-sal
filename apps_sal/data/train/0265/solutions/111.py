class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = collections.Counter()
        dp[0] = -1
        s = cnt = 0
        right = -1
        for (i, n) in enumerate(nums):
            s += n
            if s - target in dp:
                left = dp[s - target]
                if right <= left:
                    cnt += 1
                    right = i
            dp[s] = i
        return cnt
