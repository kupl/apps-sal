class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for (i, n) in enumerate(nums):
            if i < len(nums) - 1:
                if n + n > target:
                    continue
            elif n + n > target:
                continue
            if n + nums[-1] <= target:
                R = len(nums)
                cnt += 2 ** (R - i - 1)
                continue
            L = i
            R = len(nums) - 1
            while L < R:
                mid = L + (R - L) // 2
                if n + nums[mid] <= target:
                    L = mid + 1
                else:
                    R = mid
            cnt += 2 ** (R - i - 1)
        return cnt % (10 ** 9 + 7)
