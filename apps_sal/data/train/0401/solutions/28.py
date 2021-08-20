class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        snum = sum(nums)
        nums.sort()
        if not snum % 3:
            return snum
        (ones, twos) = ([], [])
        for (k, v) in enumerate(nums):
            if v % 3 == 1:
                heapq.heappush(ones, nums[k])
            if v % 3 == 2:
                heapq.heappush(twos, nums[k])
        if snum % 3 == 1:
            snum = snum - min(ones[0], sum(twos[:2])) if len(twos) >= 2 else snum - ones[0]
        if snum % 3 == 2:
            snum = snum - min(twos[0], sum(ones[:2])) if len(ones) >= 2 else snum - twos[0]
        return snum
