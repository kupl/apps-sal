class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        right = len(nums) - 1
        count = 0
        for i in range(len(nums)):
            while right > i and nums[right] > target - nums[i]:
                right -= 1
            if right == i:
                if 2 * nums[i] <= target:
                    count += 1
                return count % MOD
            else:
                count += 2 ** (right - i)
            count %= MOD
        return count % MOD
