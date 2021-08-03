class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        a = nums[0]
        b = nums[0]
        for num in nums:
            a = min(a, num)
            b = max(b, num)

        bucketSize = max(1, (b - a) // (len(nums) - 1))
        bucketNum = (b - a) // bucketSize + 1
        buckets = [[-1, -1] for i in range(bucketNum)]
        for num in nums:
            locate = (num - a) // bucketSize
            if buckets[locate][0] == -1:
                buckets[locate][0] = num
                buckets[locate][1] = num
            else:
                buckets[locate][0] = min(num, buckets[locate][0])
                buckets[locate][1] = max(num, buckets[locate][1])
        maxGap = 0
        pre = a
        for bucket in buckets:
            if bucket[0] == -1:
                continue
            maxGap = max(maxGap, bucket[0] - pre)
            pre = bucket[1]
        return maxGap
