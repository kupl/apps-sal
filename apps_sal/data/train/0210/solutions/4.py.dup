class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        n = len(nums)
        buckets = {}
        w = t + 1
        for i in range(n):
            bucket_num = nums[i] // w
            if bucket_num in buckets:
                return True
            if bucket_num - 1 in buckets and abs(nums[i] - buckets[bucket_num - 1]) < w:
                return True
            if bucket_num + 1 in buckets and abs(nums[i] - buckets[bucket_num + 1]) < w:
                return True
            buckets[bucket_num] = nums[i]
            if i >= k:
                del buckets[nums[i - k] // w]
        return False
