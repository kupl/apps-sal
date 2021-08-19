class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        M = 10 ** 9 + 7
        mismatch = 0
        nums.sort()
        base = 0
        for k in range(len(nums)):
            if nums[k] * 2 > target:
                base = bisect_left(nums, target - nums[k] + 1)
                mismatch += pow(2, k - base, M)
        return (pow(2, len(nums), M) - 1 - mismatch) % M
    '\n    def numSubseq(self, nums: List[int], target: int) -> int:\n        M = 10**9 + 7\n        pows = [1]*(len(nums)+1)\n        for k in range(1, len(pows)):\n            pows[k] = (pows[k-1]<<1) % M\n        ans = 0\n        nums.sort()\n        left = 0\n        right = len(nums) - 1\n        while left <= right:\n            total = nums[left] + nums[right]\n            if total > target:\n                right -= 1\n            else:\n                ans = (ans + pows[right-left]) % M\n                left += 1\n        return ans\n    '
    '\n    def numSubseq(self, nums: List[int], target: int) -> int:\n        from bisect import bisect_left\n        M = 10**9 + 7\n        pows = [1]*(len(nums)+1)\n        for k in range(1, len(pows)):\n            pows[k] = (pows[k-1]<<1) % M\n        ans = 0\n        nums.sort()\n        base = 0\n        for k in range(len(nums)):\n            if nums[k]*2 <= target:\n                ans += pow(2, k, M)\n            else:\n                # while base > 0 and nums[base] + nums[k] > target:\n                #     base -= 1\n                # while base < k and nums[base] + nums[k] <= target:\n                #     base += 1\n                base = bisect_left(nums, target - nums[k]+1)\n                ans += (pow(2, base, M) - 1) * pow(2, k-base, M)\n            #print(k, base, ans)\n        return ans % M\n    '
