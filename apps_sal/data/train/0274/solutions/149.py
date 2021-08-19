class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        i = 0
        j = 0
        n = len(nums)
        maxq = []
        minq = []
        max_l = 0
        while i < n and j < n:
            while maxq and nums[j] > maxq[-1]:
                maxq.pop()
            while minq and nums[j] < minq[-1]:
                minq.pop()
            maxq.append(nums[j])
            minq.append(nums[j])
            while maxq[0] - minq[0] > limit:
                if nums[i] == maxq[0]:
                    maxq.pop(0)
                if nums[i] == minq[0]:
                    minq.pop(0)
                i += 1
            max_l = max(max_l, j - i + 1)
            j += 1
        return max_l
