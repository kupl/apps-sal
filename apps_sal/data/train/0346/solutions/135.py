class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # option 1: at most
        #         def atMost(A, k):
        #             res = 0
        #             i = 0
        #             for j in range(len(A)):
        #                 k -= A[j]%2
        #                 while k < 0:
        #                     k += A[i]%2
        #                     i += 1
        #                 res += j - i + 1
        #             return res

        #         return atMost(nums, k) - atMost(nums, k-1)

        # option 2: 3 pointers
        res = i = count = 0
        for j in range(len(nums)):
            if nums[j] % 2:
                k -= 1
                count = 0

            while k == 0:
                k += nums[i] % 2
                i += 1
                count += 1

            res += count
        return res
