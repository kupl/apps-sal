class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (ret, l, r) = (0, 0, len(nums) - 1)
        (p, pw) = ([], 1)
        for d in range(len(nums)):
            p.append(pw)
            pw <<= 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                ret = (ret + p[r - l]) % (10 ** 9 + 7)
                l += 1
            else:
                r -= 1
        return ret
