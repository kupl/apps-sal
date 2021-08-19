class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            s = nums[i] + nums[j]
            if s <= target:
                ans += 2 ** (j - i)
                ans %= 10 ** 9 + 7
                i += 1
            else:
                j -= 1
        return ans
