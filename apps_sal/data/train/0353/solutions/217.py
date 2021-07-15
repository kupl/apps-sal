class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = i = 0
        while i < len(nums) and nums[i] <= target // 2:
            j = self.help(nums, target-nums[i])
            if j >= i:
                ans += 2**(j-i) % (10**9 + 7)
            i += 1
        return ans % (10**9 + 7)
    
    def help(self, nums, target):
        i, j = 0, len(nums)-1
        while i < j:
            mid = i + (j - i+ 1) // 2
            if nums[mid] <= target:
                i = mid
            else:
                j = mid - 1
        return i
        

