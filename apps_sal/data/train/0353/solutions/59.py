class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums) - 1
        ans = 0
        for i, n in enumerate(nums):
            while j >= i and n + nums[j] > target:
                j -= 1
            if j >= i:
                ans += 1 << (j - i)
                ans %= 1000000007
        return ans
