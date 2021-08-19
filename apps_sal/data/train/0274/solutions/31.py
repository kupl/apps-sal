class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        (maxq, minq) = ([], [])
        i = 0
        for num in nums:
            while maxq and maxq[-1] < num:
                maxq.pop()
            while minq and minq[-1] > num:
                minq.pop()
            maxq.append(num)
            minq.append(num)
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.pop(0)
                if minq[0] == nums[i]:
                    minq.pop(0)
                i += 1
        return len(nums) - i
