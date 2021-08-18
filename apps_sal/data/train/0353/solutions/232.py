class Solution:
    '''
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
    '''

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10**9 + 7
        ans = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            total = nums[left] + nums[right]
            if total <= target:
                ans += pow(2, right - left, M)
            if total > target:
                right -= 1
            else:
                left += 1
        return ans % M
