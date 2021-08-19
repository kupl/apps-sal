class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = -sys.maxsize
        n = len(nums)
        dp = [0] * (n + 1)
        dq = collections.deque()
        for i in range(n):
            if not dq:
                dp[i + 1] = nums[i]
            else:
                dp[i + 1] = max(nums[i], dq[0] + nums[i])
            dq.append(dp[i + 1])
            while len(dq) > k:
                dq.popleft()
            while len(dq) > 1 and dq[0] <= dq[-1]:
                dq.popleft()
            res = max(res, dp[i + 1])
        return res
