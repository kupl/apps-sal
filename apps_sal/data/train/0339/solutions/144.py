from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        nums1_sq = [num**2 for num in nums1]
        nums2_sq = [num**2 for num in nums2]

        cache = defaultdict(int)
        count = 0

        for index in range(len(nums2)):
            number = nums2[index]
            if cache[number]:
                count += cache[number]
            for sub_index in range(len(nums1_sq)):
                square = nums1_sq[sub_index]
                q, r = divmod(square, number)
                if not r:
                    cache[q] += 1

        cache = defaultdict(int)

        for index in range(len(nums1)):
            number = nums1[index]
            if cache[number]:
                count += cache[number]
            for sub_index in range(len(nums2_sq)):
                square = nums2_sq[sub_index]
                q, r = divmod(square, number)
                if not r:
                    cache[q] += 1

        return count
