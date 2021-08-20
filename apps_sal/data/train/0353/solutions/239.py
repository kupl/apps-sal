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

    def numSubseq(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        M = 10 ** 9 + 7
        pows = [1] * (len(nums) + 1)
        for k in range(1, len(pows)):
            pows[k] = (pows[k - 1] << 1) % M
        ans = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k] * 2 <= target:
                ans += pows[k]
            else:
                base = bisect_left(nums, target - nums[k] + 1)
                ans += (pows[base] - 1) * pows[k - base]
        return ans % M
    '\n    def numSubseq(self, nums: List[int], target: int) -> int:\n        M = 10**9 + 7\n        pows = [1]*(len(nums)+1)\n        for k in range(1, len(pows)):\n            pows[k] = (pows[k-1]<<1) % M\n        ans = 0\n        nums.sort()\n        left = 0\n        right = len(nums) - 1\n        while left <= right:\n            total = nums[left] + nums[right]\n            if total > target:\n                right -= 1\n            else:\n                ans = (ans + pows[right-left]) % M\n                left += 1\n        return ans\n    '
