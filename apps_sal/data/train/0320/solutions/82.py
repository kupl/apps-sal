class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Greedy
        res = 0
        max_len = 0
        for x in nums:
            bit = 0
            while x > 0:
                if x % 2 == 1:
                    res += 1
                x >>= 1
                bit += 1

            max_len = max(max_len, bit)

        return res + max_len - 1

        # TLE
#         n = len(nums)
#         arr = [0] * n
#         self.memo = {}
#         self.helper(nums)
#         # print(self.memo)
#         return self.memo[tuple(nums)]

#     def helper(self, nums):
#         if sum(nums) == 0:
#             return 0
#         if tuple(nums) in self.memo:
#             return self.memo[tuple(nums)]

#         need = sys.maxsize
#         for i in range(len(nums)):
#             if nums[i] - 1 >= 0:
#                 nums[i] -= 1
#                 need = min(need, self.helper(nums))
#                 nums[i] += 1


#         all_even = True
#         for x in nums:
#             if x % 2 != 0:
#                 all_even = False
#         if all_even:
#             temp = [x // 2 for x in nums]
#             need = min(need, self.helper(temp))

#         res = 1 + need
#         self.memo[tuple(nums)] = res
#         return res
