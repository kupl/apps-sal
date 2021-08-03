class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        m = len(nums)
        if m == 0:
            return False

        buckets = {}
        _min = 0
        for i in range(m):
            num = nums[i] - _min
            bucket = num // (t + 1)
            flag = bucket in buckets \
                or (bucket - 1 in buckets and abs(buckets[bucket - 1] - num) <= t) \
                or (bucket + 1 in buckets and abs(buckets[bucket + 1] - num) <= t)

            if flag:
                return True
            if len(buckets) >= k:
                del buckets[(nums[i - k] - _min) // (t + 1)]

            buckets[bucket] = num
        return False
