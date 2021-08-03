class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        start, end = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while start <= end:
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                res += pow(2, end - start) % mod
                start += 1
        return res % mod
