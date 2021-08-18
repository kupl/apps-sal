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

    '''
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10**9 + 7
        pows = [1]*(len(nums)+1)
        for k in range(1, len(pows)):
            pows[k] = (pows[k-1]<<1) % M
        ans = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            total = nums[left] + nums[right]
            if total > target:
                right -= 1
            else:
                ans = (ans + pows[right-left]) % M
                left += 1
        return ans
    '''

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10**9 + 7
        pows = [1] * (len(nums) + 1)
        for k in range(1, len(pows)):
            pows[k] = (pows[k - 1] << 1) % M
        ans = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k] * 2 <= target:
                ans += pow(2, k, M)
            else:
                while base > 0 and nums[base] + nums[k] > target:
                    base -= 1
                while base < k and nums[base] + nums[k] <= target:
                    base += 1
                ans += ((pow(2, base) - 1) % M) * pow(2, k - base, M)
        return ans % M
