class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = collections.deque()
        min_deque = collections.deque()

        start = 0
        end = 0
        max_limit_subarray = 0
        for end in range(len(nums)):
            while min_deque and nums[end] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(end)

            while max_deque and nums[end] > nums[max_deque[-1]]:
                max_deque.pop()

            max_deque.append(end)

            while abs(nums[max_deque[0]] - nums[min_deque[0]]) > limit:
                start += 1
                if start > min_deque[0]:
                    min_deque.popleft()
                if start > max_deque[0]:
                    max_deque.popleft()

            max_limit_subarray = max(max_limit_subarray, end - start + 1)

        return max_limit_subarray
