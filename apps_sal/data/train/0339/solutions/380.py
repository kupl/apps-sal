class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def prod_finder(num_list1, num_list2):
            prod_map = {}
            for n in num_list1:
                prod_map[n * n] = 0
            for n in num_list1:
                prod_map[n * n] += 1
            count = 0
            for i in range(0, len(num_list2)):
                for j in range(i + 1, len(num_list2)):
                    p = num_list2[i] * num_list2[j]
                    if p in prod_map:
                        count += prod_map[p]
            return count
        return prod_finder(nums1, nums2) + prod_finder(nums2, nums1)
