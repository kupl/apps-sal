class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        max_queue = collections.deque([0, ])
        max_sum = nums[0]
        for i in range(1, len(nums)):
            while max(0, i - k) > max_queue[0]:
                max_queue.popleft()
            nums[i] += max(0, nums[max_queue[0]])
            max_sum = max(max_sum, nums[i])
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()
            max_queue.append(i)

        return max_sum
