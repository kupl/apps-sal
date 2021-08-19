class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(m):
            if m < 0:
                return 0
            left = res = 0
            for (right, x) in enumerate(nums):
                m -= x & 1
                while m < 0:
                    m += nums[left] & 1
                    left += 1
                res += right - left + 1
            return res
        return atMost(k) - atMost(k - 1)
