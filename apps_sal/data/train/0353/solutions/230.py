class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        mod = 10 ** 9 + 7
        y = len(nums) - 1
        x = 0
        ans = 0
        while x <= y:
            if nums[y] + nums[x] > target:
                y -= 1
            else:
                ans = (ans + pow(2, y - x, mod)) % mod
                x += 1
        return ans
