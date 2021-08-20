class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        for ri in range(len(nums)):
            if nums[ri] + nums[0] > target:
                break
        (le, ans) = (0, 0)
        while le <= ri:
            if nums[le] + nums[ri] > target:
                ri -= 1
            else:
                cnt = 2 ** (ri - le)
                ans = (ans + cnt) % MOD
                le += 1
        return ans
