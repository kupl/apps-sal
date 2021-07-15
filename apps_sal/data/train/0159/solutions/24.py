class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dp = [0]*n
        q = deque()
        ans = float('-inf')
        for i in range(n):
            if i>k and q[0]==i-k-1:
                q.popleft()
            dp[i]= (0 if len(q)==0 else max(dp[q[0]],0)) + nums[i]
            while len(q)>0 and dp[i]>=dp[q[-1]]:
                q.pop()
            q.append(i)
            ans = max(ans, dp[i])
        return ans
