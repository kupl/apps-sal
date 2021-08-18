class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        while left < len(nums) and nums[left] != 1:
            left += 1

        right = left
        while right + 1 < len(nums) and nums[right + 1] == 1:
            right += 1

        if right == len(nums):
            return 0

        maxOnes = right - left + 1

        while left < len(nums):
            left = right + 1
            while left < len(nums) and nums[left] != 1:
                left += 1

            right = left
            while right + 1 < len(nums) and nums[right + 1] == 1:
                right += 1

            maxOnes = max(maxOnes, right - left + 1)

        return maxOnes

    def longestOnes(self, A: List[int], K: int) -> int:
        if K == 0:
            return self.findMaxConsecutiveOnes(A)

        if len(A) == 0:
            return 0

        left, right = 0, 0

        if A[right] == 0:
            K -= 1
        while right + 1 < len(A) and K > 0:
            right += 1
            if A[right] == 0:
                K -= 1

        while right + 1 < len(A) and A[right + 1] == 1:
            right += 1

        maxSize = right - left + 1

        while right < len(A):
            while left < len(A) and A[left] != 0:
                left += 1
            if left < len(A):
                left += 1
            else:
                return maxSize

            right += 1
            while right + 1 < len(A) and A[right + 1] == 1:
                right += 1

            maxSize = max(maxSize, right - left + 1)

        return maxSize
