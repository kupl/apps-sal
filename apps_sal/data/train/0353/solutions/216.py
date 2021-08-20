class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        mod = 1000000007
        st = 0
        ed = len(nums) - 1
        while st < ed:
            while nums[st] + nums[ed] > target:
                ed -= 1
            if st < ed:
                ans += 2 ** (ed - st) - 1
                ans %= mod
            st += 1
        for i in range(len(nums)):
            if 2 * nums[i] <= target:
                ans += 1
        return ans % mod
