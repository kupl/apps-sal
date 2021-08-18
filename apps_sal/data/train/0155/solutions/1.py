class Solution:
    def maxJumps(self, nums: List[int], d: int) -> int:
        nums.append(math.inf)
        dp = [1] * len(nums)
        stack = []
        for i, cur in enumerate(nums):
            while stack and nums[stack[-1]] < cur:
                poped_same_val = [stack.pop()]
                while stack and nums[stack[-1]] == nums[poped_same_val[0]]:
                    poped_same_val.append(stack.pop())
                for poped in poped_same_val:
                    if i - poped <= d:
                        dp[i] = max(dp[i], dp[poped] + 1)
                    if stack and poped - stack[-1] <= d:
                        left_first_big_of_poped = stack[-1]
                        dp[left_first_big_of_poped] = max(dp[left_first_big_of_poped], dp[poped] + 1)
            stack.append(i)
        return max(dp[:-1])
