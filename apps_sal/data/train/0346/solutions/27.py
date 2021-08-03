class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = i = res = 0
            for j, v in enumerate(nums):
                if v % 2:
                    count += 1
                while count > k:
                    if nums[i] % 2:
                        count -= 1
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)
