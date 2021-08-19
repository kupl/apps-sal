class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.search(nums, mid, threshold) > 0:
                r = mid
            elif self.search(nums, mid, threshold) < 0:
                l = mid
        if self.search(nums, l, threshold) >= 0:
            return l
        else:
            return r

    def search(self, nums, i, threshold):
        insum = sum([math.ceil(el / i) for el in nums])
        if insum <= threshold:
            return 1
        else:
            return -1
