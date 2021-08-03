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

        def helper(n, nums, memo):
            if n in memo:
                return memo[n]

            result = 0

            for i in range(len(nums)):
                if n % nums[i] != 0:
                    continue

                target = n // nums[i]

                lower = lowerbound(target, i + 1, len(nums), nums)
                higher = higherbound(target, i + 1, len(nums), nums)

                result += (higher - lower)

            memo[n] = result
            return result

        result = 0

        memo1 = {}
        for n in nums1:
            result += helper(n * n, nums2, memo1)

        memo2 = {}
        for n in nums2:
            result += helper(n * n, nums1, memo2)

        return result
