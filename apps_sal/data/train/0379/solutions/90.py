from functools import lru_cache


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        MOD = 10**9 + 7

        num_to_index1 = defaultdict(list)
        num_to_index2 = defaultdict(list)

        for i, num in enumerate(nums1):
            num_to_index1[num].append(i)
        for i, num in enumerate(nums2):
            num_to_index2[num].append(i)

        @lru_cache(None)
        def recurse(i, j):
            if i == 1 and j == len(nums1) - 1:
                return nums1[j]
            if i == 2 and j == len(nums2) - 1:
                return nums2[j]

            if i == 1:
                option1 = nums1[j] + recurse(1, j + 1)
                next_ind = num_to_index2.get(nums1[j + 1], [])
                if next_ind:
                    next_ind = next_ind[0]
                    option2 = nums1[j] + recurse(2, next_ind)
                    return max(option1, option2)
                return option1

            if i == 2:
                option1 = nums2[j] + recurse(2, j + 1)
                next_ind = num_to_index1.get(nums2[j + 1], [])
                if next_ind:
                    next_ind = next_ind[0]
                    option2 = nums2[j] + recurse(1, next_ind)
                    return max(option1, option2)
                return option1

        return max(recurse(1, 0), recurse(2, 0)) % MOD
