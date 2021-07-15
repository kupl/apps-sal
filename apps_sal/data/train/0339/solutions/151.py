class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def one_type(nums1, nums2):
            res, counter = 0, collections.Counter(nums2)
            for num1 in nums1:
                prod = num1 * num1
                for num2 in nums2:
                    target = prod / num2
                    if target in counter:
                        res += counter[target] - (target == num1)
            return res // 2

        return one_type(nums1, nums2) + one_type(nums2, nums1)
