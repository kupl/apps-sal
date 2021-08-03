class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.triplets(nums1, nums2) + self.triplets(nums2, nums1)

    def triplets(self, nums1, nums2):
        nums1_sq = [x * x for x in nums1]
        n_triplets = 0
        for i in range(len(nums1_sq)):
            nums2_lookup = {}
            for j in range(len(nums2)):
                if nums1_sq[i] % nums2[j] != 0:
                    continue
                num_to_look_for = nums1_sq[i] / nums2[j]
                count = nums2_lookup.get(num_to_look_for, 0)
                n_triplets += count
                if nums2[j] in nums2_lookup:
                    nums2_lookup[nums2[j]] += 1
                else:
                    nums2_lookup[nums2[j]] = 1

        return n_triplets
