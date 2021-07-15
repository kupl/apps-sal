class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i] = nums[i] + max(dp[j] j - i <= k)
        # max(dp)
        n = len(nums)
        from collections import deque
        q = deque()
        q.append((nums[-1], n-1))
        ans = nums[-1]
        for i in reversed(list(range(n-1))):
            while q and q[0][1] - i > k:
                q.popleft()
            dp = nums[i]
            if q:
                dp = max(dp, nums[i] + q[0][0])
            ans = max(dp, ans)
            while q and q[-1][0] <= dp:
                q.pop()
            q.append((dp, i))
        return ans
        

