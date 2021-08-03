class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [-math.inf] * N

        q = deque()  # . Val, Index
        for i in range(N):
            dp[i] = max(dp[i], nums[i] + (q[0][0] if q else 0), nums[i])

            while q and dp[i] > q[-1][0]:
                q.pop()
            while q and i - q[0][1] >= k:
                q.popleft()
            q.append((dp[i], i))

        # print(dp)
        return max(dp)
