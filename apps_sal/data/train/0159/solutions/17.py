class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        deq = deque([0])
        for i in range(n):
            if deq and deq[0] < i - k:
                deq.popleft()
            while deq and nums[i] + dp[deq[0]] > dp[deq[-1]]:
                a = deq.pop()
            dp[i] = max(nums[i], nums[i] + dp[deq[0]] if deq else nums[i] + dp[a])
            deq.append(i)

        return max(dp)
