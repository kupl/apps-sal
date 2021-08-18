class Solution:
    '''
    def numSubseq(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        M = 10**9 + 7
        mismatch = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k]*2 > target:
                base = bisect_left(nums, target - nums[k]+1)
                mismatch += pow(2, k-base, M)
        return (pow(2, len(nums), M) - 1 - mismatch) % M
    '''

    '''   
    def numSubseq(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        M = 10**9 + 7
        pows = [1]*(len(nums)+1)
        for k in range(1, len(pows)):
            pows[k] = (pows[k-1]<<1) % M
        ans = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k]*2 <= target:
                ans += pows[k]
            else:
                base = bisect_left(nums, target - nums[k]+1)
                ans += (pows[base]-1)*pows[k-base]
        return ans % M
    '''

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10**9 + 7
        pows = [1] * (len(nums) + 1)
        for k in range(1, len(pows)):
            pows[k] = (pows[k - 1] << 1) % M
        ans = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            total = nums[left] + nums[right]
            if total > target:
                right -= 1
            else:
                ans = (ans + pows[right - left]) % M
                left += 1
        return ans
