class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        (l, r) = (0, len(nums) - 1)
        cnt = 0
        mod = pow(10, 9) + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                cnt += pow(2, r - l)
                cnt = cnt % mod
                l += 1
        return cnt
