class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        cumsum = 0
        cache = set([0])
        for num in nums:
            cumsum += num
            if cumsum - target in cache:
                res += 1
                cache = set()
            cache.add(cumsum)
        return res
