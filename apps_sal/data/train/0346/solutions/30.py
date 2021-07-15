class Solution:
    def numberOfSubarrays(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    
    def atMost(self, nums, k):
        if k < 0:
            return 0
        n = len(nums)
        right = 0
        res = 0
        cnt = 0
        for left in range(n):
            while right <= n - 1 and (cnt < k or nums[right] % 2 == 0):
                cnt += (nums[right] % 2 == 1)
                right += 1
            res += right - left
            cnt -= (nums[left] % 2 == 1)
        return res
