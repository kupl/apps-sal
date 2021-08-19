class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMostK(nums, K):
            res = 0
            b = 0
            oddCount = 0
            for e in range(len(nums)):
                oddCount += int(nums[e] % 2 == 1)
                while oddCount > K:
                    oddCount -= int(nums[b] % 2 == 1)
                    b += 1
                res += e - b + 1
            return res
        return atMostK(nums, k) - atMostK(nums, k - 1)
