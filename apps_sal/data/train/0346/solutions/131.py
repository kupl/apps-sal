class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        right_pointer = -1
        count = 0
        odd = 0

        while right_pointer < len(nums) - 1:
            right_pointer += 1

            if nums[right_pointer] % 2 == 1:
                odd += 1

            if odd == k:
                left_side = 1
                right_side = 1

                while right_pointer < len(nums) - 1 and nums[right_pointer + 1] % 2 == 0:
                    right_side += 1
                    right_pointer += 1

                while left_pointer <= right_pointer and nums[left_pointer] % 2 == 0:
                    left_side += 1
                    left_pointer += 1

                count += left_side * right_side
                left_pointer += 1
                odd -= 1

        return count

# def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#     i = count = nice_count = odd_count = 0
#     for j in range(len(nums)):
#         if nums[j] % 2 == 1:
#             odd_count += 1
#             if odd_count == k:
#                 count = 0
#                 while odd_count == k:
#                     if nums[i] % 2 == 1:
#                         odd_count -= 1
#                     i += 1
#                     count += 1
#         nice_count += count

#     return nice_count
