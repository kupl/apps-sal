from collections import defaultdict


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def helper(k):
            start = end = counter = res = 0
            while end < len(nums):
                if nums[end] % 2 != 0:
                    counter += 1
                end += 1
                while counter > k:
                    if nums[start] % 2 != 0:
                        counter -= 1
                    start += 1
                res += end - start
            return res
        return helper(k) - helper(k - 1)
