class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(nums, k):
            i, j, count, res = 0, 0, 0, 0
            while j < len(nums):
                if nums[j] % 2 == 1:
                    count += 1
                while count > k:
                    if nums[i] % 2 == 1:
                        count -= 1
                    i += 1
                res += j - i + 1
                j += 1
            return res

        return at_most(nums, k) - at_most(nums, k - 1)
