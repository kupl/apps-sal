class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_stack = []
        min_stack = []
        l = 0
        ans = 0
        for r in range(len(nums)):
            while max_stack and nums[max_stack[-1]] < nums[r]:
                max_stack.pop()
            max_stack.append(r)
            while min_stack and nums[min_stack[-1]] > nums[r]:
                min_stack.pop()
            min_stack.append(r)
            while max_stack and min_stack and (nums[max_stack[0]] - nums[min_stack[0]] > limit):
                if max_stack[0] <= l:
                    max_stack.pop(0)
                if min_stack[0] <= l:
                    min_stack.pop(0)
                l += 1
            ans = max(ans, r - l + 1)
        return ans
