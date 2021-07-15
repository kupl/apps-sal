class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        output, nums = 0, sorted(nums)
        while l <= r:
            if nums[l] + nums[r] <= target:
                output += pow(2, r - l, 10 ** 9 + 7)
                l += 1
            else:
                r -= 1
        return output % (10 ** 9 + 7)
    
    # def numSubseq(self, A, target):
    #     A.sort()
    #     l, r = 0, len(A) - 1
    #     res = 0
    #     mod = 10**9 + 7
    #     while l <= r:
    #         if A[l] + A[r] > target:
    #             r -= 1
    #         else:
    #             res += pow(2, r - l, mod)
    #             l += 1
    #     return res % mod

