class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = float('-inf')
        for (j, x) in enumerate(nums):
            if x:
                if j - i <= k:
                    return False
                i = j
        return True
