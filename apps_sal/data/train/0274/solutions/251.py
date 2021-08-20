class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (minq, maxq) = (deque(), deque())
        i = 0
        for num in nums:
            while minq and minq[-1] > num:
                minq.pop()
            while maxq and maxq[-1] < num:
                maxq.pop()
            minq.append(num)
            maxq.append(num)
            if maxq[0] - minq[0] > limit:
                if nums[i] == minq[0]:
                    minq.popleft()
                if nums[i] == maxq[0]:
                    maxq.popleft()
                i += 1
        return len(nums) - i
