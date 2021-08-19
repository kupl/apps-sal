class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [i % 2 for i in nums]
        ans = 0
        tmp = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 1:
                k -= 1
                tmp = 0
            while k == 0:
                k += nums[l]
                l += 1
                tmp += 1
            ans += tmp
        return ans
