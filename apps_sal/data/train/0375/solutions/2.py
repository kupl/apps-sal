class Solution:

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        (left, right) = (min(nums), max(nums))
        brng = (right - left) // (len(nums) - 1) + 1
        bnum = (right - left) // brng + 1
        bucket = [None] * bnum
        for x in nums:
            idx = (x - left) // brng
            if bucket[idx]:
                bucket[idx] = (min(bucket[idx][0], x), max(bucket[idx][1], x))
            else:
                bucket[idx] = (x, x)
        max_gap = pre = 0
        for cur in range(1, bnum):
            if not bucket[cur]:
                continue
            max_gap = max(max_gap, bucket[cur][0] - bucket[pre][1])
            pre = cur
        return max_gap
