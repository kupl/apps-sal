class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[0] = nums[0]
        maxDeque = deque()
        ans = -sys.maxsize
        for j in range(n):
            while len(maxDeque) > 0 and j - maxDeque[0] > k:
                maxDeque.popleft()
            preMax = dp[maxDeque[0]] if len(maxDeque) > 0 else 0
            dp[j] = max(preMax + nums[j], nums[j])
            ans = max(dp[j], ans)
            while len(maxDeque) > 0 and dp[maxDeque[-1]] < dp[j]:
                maxDeque.pop()
            maxDeque.append(j)
        return ans
