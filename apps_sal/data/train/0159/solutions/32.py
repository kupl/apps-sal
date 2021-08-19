class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [-math.inf for i in range(n)]
        dp[0] = nums[0]
        ans = [nums[0]]
        queue = [0]
        for i in range(1, n):
            dp[i] = max(dp[i], nums[i], nums[i] + ans[i - 1])
            if len(queue) == 0:
                queue.append(i)
            else:
                while len(queue) > 0 and (dp[i] > dp[queue[-1]] or i - queue[0] >= k):
                    if dp[i] > dp[queue[-1]]:
                        queue.pop(-1)
                    else:
                        queue.pop(0)
                queue.append(i)
            ans.append(dp[queue[0]])
        return max(dp)
