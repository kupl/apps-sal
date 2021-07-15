class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ri = n - 1
        ans = 0
        for li, l in enumerate(nums):
            if l * 2 > target: break
            while nums[ri] + l > target:
                ri -= 1
            ans = (ans + pow(2, ri - li, 1000000007)) % 1000000007
        return ans
