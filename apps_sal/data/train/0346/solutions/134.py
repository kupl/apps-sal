class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        count = {0: 0, 1: 0}
        res = i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                k -= 1
            while k < 0:
                if nums[i] % 2 == 1:
                    k += 1
                i += 1
            res += j - i + 1
        return res
