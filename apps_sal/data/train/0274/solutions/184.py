class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        if nums is None or len(nums) == 0:
            return 0

        queue = collections.deque([])
        max_len = 0
        right = 0
        min_heap = []
        max_heap = []
        for left in range(len(nums)):
            if left == right:
                heapq.heappush(min_heap, (nums[left], left))
                heapq.heappush(max_heap, (-nums[left], left))
                right += 1

            while right < len(nums):
                cur_min = min_heap[0][0]
                cur_max = -max_heap[0][0]
                if (abs(nums[right] - cur_min) > limit):
                    break
                if (abs(nums[right] - cur_max) > limit):
                    break
                heapq.heappush(min_heap, (nums[right], right))
                heapq.heappush(max_heap, (-nums[right], right))
                right += 1

            max_len = max(max_len, right - left)
            if right == len(nums):
                return max_len

            while max_heap and max_heap[0][1] <= left:
                heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= left:
                heapq.heappop(min_heap)

        return max_len
