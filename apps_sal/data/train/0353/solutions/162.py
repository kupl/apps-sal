class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        right = n - 1
        for i in range(len(nums)):
            if nums[i] > target or right < i:
                break
            while right >= i and nums[i] + nums[right] > target:
                right -= 1
            if right < i:
                break
            if nums[i] + nums[right] <= target:
                total = (total + 2 ** (right - i)) % (10**9 + 7)

        return int(total) % (10**9 + 7)
