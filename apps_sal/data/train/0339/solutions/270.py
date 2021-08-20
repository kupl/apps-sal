class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.triplets(nums1, nums2) + self.triplets(nums2, nums1)

    def triplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        counter = Counter(nums2)
        for i in range(len(nums1)):
            target = nums1[i] ** 2
            for j in range(len(nums2)):
                if target / nums2[j] in counter:
                    if target / nums2[j] == nums2[j]:
                        count += counter[target / nums2[j]] - 1
                    else:
                        count += counter[target / nums2[j]]
        return int(count / 2)
