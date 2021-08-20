class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (s, e) = (0, len(nums) - 1)
        mod = 10 ** 9 + 7
        result = 0
        while s <= e:
            if nums[s] + nums[e] <= target:
                result += pow(2, e - s, mod)
                s += 1
            else:
                e -= 1
        return result % mod
