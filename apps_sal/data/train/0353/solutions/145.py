class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        rgt = N - 1
        for lft in range(N):
            if nums[lft] * 2 > target:
                break

            lo, hi = lft, N - 1
            while lo + 1 < hi:
                m = (lo + hi) // 2
                if nums[lft] + nums[m] <= target:
                    lo = m
                else:
                    hi = m

            if nums[lft] + nums[hi] > target:
                ans += 2**(lo - lft)
            else:
                ans += 2**(hi - lft)

        return ans % (10**9 + 7)
