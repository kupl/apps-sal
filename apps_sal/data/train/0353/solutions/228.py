class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        mod = 10**9 + 7
        while i <= j:
            minv = nums[i]
            maxv = nums[j]
            sumv = minv + maxv
            if sumv > target:
                j -= 1
            else:
                count = (count + pow(2, j - i, mod)) % mod
                i += 1
        return count
