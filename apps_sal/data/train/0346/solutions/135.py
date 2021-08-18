class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        res = i = count = 0
        for j in range(len(nums)):
            if nums[j] % 2:
                k -= 1
                count = 0

            while k == 0:
                k += nums[i] % 2
                i += 1
                count += 1

            res += count
        return res
