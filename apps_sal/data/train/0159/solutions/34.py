class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # 用来保留k步内的累加最大值
        deque = collections.deque()
        for i in range(len(nums)):
            if deque:
                nums[i] += deque[0]

            while deque and nums[i] > deque[-1]:
                deque.pop()

            if nums[i] > 0:
                deque.append(nums[i])
            # 去除超过k步的最大值，为下一步要加的的最大值做准备
            if i >= k and deque and deque[0] == nums[i - k]:
                deque.popleft()

        return max(nums)
