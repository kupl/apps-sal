class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        nums2.sort()

        def lowerbound(target, left, right, nums):
            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        def higherbound(target, left, right, nums):
            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        @lru_cache(maxsize=None)
        def helper1(n):
            result = 0

            for i in range(len(nums1)):
                if n % nums1[i] != 0:
                    continue

                target = n // nums1[i]

                lower = lowerbound(target, i + 1, len(nums1), nums1)
                higher = higherbound(target, i + 1, len(nums1), nums1)

                result += (higher - lower)

            return result

        @lru_cache(maxsize=None)
        def helper2(n):
            result = 0

            for i in range(len(nums2)):
                if n % nums2[i] != 0:
                    continue

                target = n // nums2[i]

                lower = lowerbound(target, i + 1, len(nums2), nums2)
                higher = higherbound(target, i + 1, len(nums2), nums2)

                result += (higher - lower)

            return result

        result = 0
        for n in nums1:
            result += helper2(n * n)

        for n in nums2:
            result += helper1(n * n)

        return result
