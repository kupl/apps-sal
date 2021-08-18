class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n % 2 for n in nums]

        def atMost(k):
            ans, j = 0, 0
            for i, n in enumerate(nums):
                k -= n
                while k < 0:
                    k += nums[j]
                    j += 1
                ans += i - j + 1
            return ans

        return atMost(k) - atMost(k - 1)
