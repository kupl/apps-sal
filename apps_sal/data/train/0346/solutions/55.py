class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        odd = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] & 1:
                odd += 1
                if odd >= k:
                    count = 1
                    if odd > k:
                        j += 1
                        odd -= 1
                    while nums[j] & 1 == 0:
                        j += 1
                        count += 1
                res += count
            else:
                res += count
        return res

