class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(k):
            ans = i = 0
            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                ans += j - i + 1
            return ans
        return helper(k) - helper(k - 1)
