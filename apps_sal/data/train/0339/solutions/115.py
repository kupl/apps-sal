class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import defaultdict
        if len(nums1) == 1 and len(nums2) == 1:
            return 0

        def twoproduct(nsquare, nums):
            countmap = defaultdict(int)
            total = 0
            for num in nums:
                if nsquare % num == 0:
                    total += countmap.get(nsquare // num, 0)
                    countmap[num] += 1
            return total
        ans = 0
        for num in nums1:
            ans += twoproduct(num**2, nums2)
        for num in nums2:
            ans += twoproduct(num**2, nums1)
        return ans
