class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10**9 + 7
        mismatch = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k]*2 > target:
                while base > 0 and nums[base] + nums[k] > target:
                    base -= 1
                while base < k and nums[base] + nums[k] <= target:
                    base += 1
                mismatch += pow(2, k-base, M)
        return (pow(2, len(nums), M) - 1 - mismatch) % M
