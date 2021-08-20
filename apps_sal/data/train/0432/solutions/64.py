from collections import Counter, defaultdict


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        nums = Counter(nums)
        while nums:
            x = min(nums)
            min_count = nums[x]
            del nums[x]
            for i in range(1, k):
                if nums[x + i] < min_count:
                    return False
                else:
                    nums[x + i] -= min_count
                    if nums[x + i] == 0:
                        del nums[x + i]
        return True
