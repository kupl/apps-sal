class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (min_heap, max_heap) = (deque([0]), deque([0]))
        res = 1
        far = -1
        for i in range(1, len(nums)):
            while min_heap and nums[min_heap[-1]] > nums[i]:
                min_heap.pop()
            while max_heap and nums[max_heap[-1]] < nums[i]:
                max_heap.pop()
            while min_heap and abs(nums[min_heap[0]] - nums[i]) > limit:
                far = max(far, min_heap.popleft())
            while max_heap and abs(nums[max_heap[0]] - nums[i]) > limit:
                far = max(far, max_heap.popleft())
            res = max(res, i - far)
            min_heap.append(i)
            max_heap.append(i)
        return res
