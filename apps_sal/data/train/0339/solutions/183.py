class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        set1 = set(nums1)
        set2 = set(nums2)
        lookup1 = defaultdict(int)

        def ncr(n, r):
            from math import factorial
            return factorial(n) // factorial(r) // factorial(n - r)

        def countTriplets(nums1, nums2):
            lookup = defaultdict(int)
            count = 0
            for index, val in enumerate(nums1):
                target = val**2
                lookup = defaultdict(int)
                for index2, val2 in enumerate(nums2):
                    if target % val2 == 0:
                        if target // val2 in lookup:
                            count += lookup[target // val2]
                    lookup[val2] += 1
            return count

        # solving type 1
        count1 = countTriplets(nums1, nums2)
        count2 = countTriplets(nums2, nums1)
        return count1 + count2
