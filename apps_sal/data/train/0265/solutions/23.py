class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cache = set([0])
        (cur, res) = (0, 0)
        for i in range(len(nums)):
            cur += nums[i]
            if cur - target in cache:
                res += 1
                cache.clear()
            cache.add(cur)
        return res
