from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def find_triplets(nums_1, nums_2):
            ans = 0
            target = list(map(lambda x: x**2, nums_1))
            count = Counter(target)
            for j in range(len(nums_2)):
                for k in range(j + 1, len(nums_2)):
                    if nums_2[j] * nums_2[k] in count:
                        ans += count[nums_2[j] * nums_2[k]]
            return ans

        return find_triplets(nums1, nums2) + find_triplets(nums2, nums1)
