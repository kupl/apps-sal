class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        j = len(nums) - 1
        mod = 10**9 + 7

        for i in range(len(nums)):
            if nums[i] > target:
                break
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                break
            if i == j:
                res += 1
                continue
            n = j - i
            res += (2**n) % mod
        return res % mod
