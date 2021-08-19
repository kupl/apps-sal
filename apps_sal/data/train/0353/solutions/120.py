class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        ans = 0
        mod = 10 ** 9 + 7
        while start <= end:
            while nums[start] + nums[end] > target:
                end -= 1
                if start > end:
                    return ans % mod
            ans += 2 ** (end - start)
            start += 1
        return ans % mod
