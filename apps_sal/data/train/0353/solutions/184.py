class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        right = len(nums) - 1
        count = 0
        for i in range(len(nums)):
            while right >= i and nums[i] + nums[right] > target:
                right -= 1
            if right < i:
                break
            else:
                count += 2 ** (right - i)
            count %= MOD
        return count % MOD
