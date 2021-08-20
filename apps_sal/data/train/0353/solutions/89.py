class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while True:
            while r >= l and nums[l] + nums[r] > target:
                r = r - 1
            if l <= r:
                res = res + 2 ** (r - l)
            else:
                break
            l = l + 1
        return res % (10 ** 9 + 7)
