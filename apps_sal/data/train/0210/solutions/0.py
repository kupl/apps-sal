class Solution:

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) < 2 or k <= 0 or t < 0:
            return False
        if t == 0:
            visited = set()
            for (i, n) in enumerate(nums):
                if n in visited:
                    return True
                visited.add(n)
                if i >= k:
                    visited.remove(nums[i - k])
            return False
        bucket = {}
        for (i, n) in enumerate(nums):
            b = n // t
            if b in bucket:
                return True
            if b + 1 in bucket and abs(bucket[b + 1] - n) <= t:
                return True
            if b - 1 in bucket and abs(bucket[b - 1] - n) <= t:
                return True
            bucket[b] = n
            if i >= k:
                del bucket[nums[i - k] // t]
        return False
