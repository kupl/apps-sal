class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = count = l = 0

        for num in nums:
            if num & 1:
                k -= 1
                count = 0

            while k == 0:
                k += nums[l] & 1
                count += 1
                l += 1

            ans += count

        return ans
