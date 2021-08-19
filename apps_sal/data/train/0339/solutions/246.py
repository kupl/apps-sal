class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        for x in nums1:
            seen = {}
            v = x * x
            for i in nums2:
                if i in seen:
                    count += seen[i]
                seen[v / i] = seen.get(v / i, 0) + 1
        for x in nums2:
            seen = {}
            v = x * x
            for i in nums1:
                if i in seen:
                    count += seen[i]
                seen[v / i] = seen.get(v / i, 0) + 1
        return count
