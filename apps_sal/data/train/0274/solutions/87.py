class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        max_stack = collections.deque([0])
        min_stack = collections.deque([0])
        (begin, end, longest) = (0, 0, 0)
        while end < n:
            while True:
                diff = nums[max_stack[0]] - nums[min_stack[0]]
                if diff > limit:
                    if min_stack[0] == begin:
                        min_stack.popleft()
                    if max_stack[0] == begin:
                        max_stack.popleft()
                    begin += 1
                else:
                    longest = max(longest, end - begin + 1)
                    break
            end += 1
            if end < n:
                while min_stack and nums[end] <= nums[min_stack[-1]]:
                    min_stack.pop()
                min_stack.append(end)
                while max_stack and nums[end] >= nums[max_stack[-1]]:
                    max_stack.pop()
                max_stack.append(end)
        return longest
