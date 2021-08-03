class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddnum = 0
        l, n = 0, len(nums)
        add = 1
        sums = 0
        for r in range(n):
            if nums[r] % 2 == 1:
                k -= 1
            while l < r and (k < 0 or nums[l] % 2 == 0):
                if k < 0:
                    add = 1
                else:
                    add += 1
                if nums[l] % 2 == 1:
                    k += 1
                l += 1
            if k == 0:
                sums += add
        return sums
