class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ans = 0
        cnt = 0
        lo = 0
        hi = 0
        cnt += nums[0] % 2
        while lo <= hi and hi < len(nums):
            if cnt < k:
                hi += 1
                if hi < len(nums) and nums[hi] % 2:
                    cnt += 1
            elif cnt > k:
                if lo < hi and nums[lo] % 2:
                    cnt -= 1
                lo += 1
            else:
                ans += 1
                tempHi = hi
                while tempHi + 1 < len(nums) and nums[tempHi + 1] % 2 == 0:
                    ans += 1
                    tempHi += 1
                if lo < len(nums) and nums[lo] % 2:
                    cnt -= 1
                lo += 1
                if hi < lo:
                    hi = lo
                    if hi < len(nums) and nums[hi] % 2:
                        cnt += 1
        return ans
