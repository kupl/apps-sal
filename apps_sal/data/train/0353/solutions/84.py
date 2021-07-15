from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int: 
        res = 0
        end = len(nums)-1
        nums.sort()
        for start in range(len(nums)):
            while nums[start] + nums[end] > target:
                if end > start:
                    end -= 1
                else:
                    return res % (10**9 + 7)
            res += 2 ** (end - start)
        return res % (10**9 + 7)
