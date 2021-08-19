class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] * 2 > target:
                break
            (l, r) = (i, len(nums) - 1)
            while l + 1 < r:
                mid = (l + r) // 2
                if nums[i] + nums[mid] > target:
                    r = mid
                else:
                    l = mid
            if nums[i] + nums[r] <= target:
                ind = r
            else:
                ind = l
            ans += 2 ** (ind - i)
        return ans % (10 ** 9 + 7)
