class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        rlt = 1
        q = collections.deque([nums[0]])
        max_stack, min_stack = [nums[0]], [nums[0]]
        for i in range(1, len(nums)):
            while max_stack and (max_stack[0] - nums[i] > limit or
                                 nums[i] - min_stack[0] > limit):
                head = q.popleft()
                if head == max_stack[0]:
                    max_stack.pop(0)
                if head == min_stack[0]:
                    min_stack.pop(0)
            q.append(nums[i])
            while max_stack and max_stack[-1] < nums[i]:
                max_stack.pop()
            while min_stack and min_stack[-1] > nums[i]:
                min_stack.pop()
            max_stack.append(nums[i])
            min_stack.append(nums[i])
            rlt = max(rlt, len(q))

        return rlt
