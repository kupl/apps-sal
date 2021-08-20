class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def countTriplets(nums1, nums2):
            count = 0
            for (index, val) in enumerate(nums1):
                target = int(val ** 2)
                lookup = defaultdict(int)
                for (index2, val2) in enumerate(nums2):
                    if target % val2 == 0 and target // val2 in lookup:
                        count += lookup[target // val2]
                    lookup[val2] += 1
            return count
        count1 = countTriplets(nums1, nums2)
        count2 = countTriplets(nums2, nums1)
        return count1 + count2
