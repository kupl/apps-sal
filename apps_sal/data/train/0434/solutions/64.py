class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #         if len(nums) == 1:
        #             return 0
        #         ones = []
        #         count = 0

        #         for num in nums:
        #             if num == 1:
        #                 count += 1
        #             else:
        #                 if count != 0:
        #                     ones.append(count)
        #                 ones.append(0)
        #                 count = 0

        #         if count != 0:
        #             ones.append(count)

        #         print(ones)

        #         if len(ones) == 1:
        #             return max(ones) - 1
        #         m = max(ones)

        #         for i in range(1, len(ones) - 1):
        #             if ones[i] == 0:
        #                 m = max([m, ones[i - 1] + ones[i + 1]])

        #         return m

        i, r = 0, 1

        for j in range(len(nums)):
            if nums[j] == 0:
                r -= 1

            if r < 0:
                print('yes')
                if nums[i] == 0:
                    r += 1
                i += 1

        return j - i
