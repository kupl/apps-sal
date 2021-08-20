class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        i = j = 0
        while i <= j:
            while k > 0 and j < len(nums):
                if nums[j] % 2 == 1:
                    k -= 1
                j += 1
            if k != 0:
                return res
            res += 1
            t = j
            while t < len(nums):
                if nums[t] % 2 == 0:
                    res += 1
                    t += 1
                else:
                    break
            if nums[i] % 2 == 1:
                k += 1
            i += 1
        return res
