class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def cntProduct(square: int, nums: List[int]) -> int:
            (num_count, cnt) = ({}, 0)
            for num in nums:
                if square % num == 0:
                    cnt += num_count.get(square // num, 0)
                num_count[num] = 1 + num_count.get(num, 0)
            return cnt
        return sum((cntProduct(num ** 2, nums2) for num in nums1)) + sum((cntProduct(num ** 2, nums1) for num in nums2))
