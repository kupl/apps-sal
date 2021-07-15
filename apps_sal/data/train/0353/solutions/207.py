class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        m = 10**9+7
        ans = 0
        i, j = 0, len(nums)-1
        nums.sort()
        pi, pj = -1, -1
        while (pi, pj) != (i, j):
            pi, pj = i, j
            while j > i and nums[i] + nums[j] > target:
                j -= 1

            while i <= j and nums[i] + nums[j] <= target:
                ans = (ans + 2**(j-i)) % m
                i += 1
        
        return ans
