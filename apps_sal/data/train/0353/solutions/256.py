class Solution:
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        M = 10**9 + 7
        mismatch = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k]*2 > target:
                # while base > 0 and nums[base] + nums[k] > target:
                #     base -= 1
                # while base < k and nums[base] + nums[k] <= target:
                #     base += 1
                base = bisect_left(nums, target - nums[k]+1)
                mismatch += pow(2, k-base, M)
        return (pow(2, len(nums), M) - 1 - mismatch) % M
    """
    '   \n    def numSubseq(self, nums: List[int], target: int) -> int:\n        from bisect import bisect_left\n        M = 10**9 + 7\n        pows = [1]*(len(nums)+1)\n        for k in range(1, len(pows)):\n            pows[k] = (pows[k-1]<<1) % M\n        ans = 0\n        nums.sort()\n        base = 0\n        for k in range(len(nums)):\n            if nums[k]*2 <= target:\n                ans += pows[k]\n            else:\n                # while base > 0 and nums[base] + nums[k] > target:\n                #     base -= 1\n                # while base < k and nums[base] + nums[k] <= target:\n                #     base += 1\n                base = bisect_left(nums, target - nums[k]+1)\n                ans += (pows[base]-1)*pows[k-base]\n            #print(k, base, ans)\n        return ans % M\n    '

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7
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
