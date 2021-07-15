class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dp = [0] * (len(nums) + 1)
        mem = dict()
        mem[0] = -1
        cur = 0
        for i in range(1, len(nums) + 1):
            dp[i] = dp[i - 1]
            cur += nums[i - 1]
            t = cur - target
            #print(i-1, cur, t, mem)
            if t in mem:
                dp[i] = max(dp[i], dp[mem[t]] + 1)
                #print('!!', i, dp)
            mem[cur] = i
        return dp[-1]
        

