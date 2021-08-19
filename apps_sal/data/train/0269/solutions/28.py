class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        import numpy as np
        ones = np.nonzero(nums)[0]
        if ones.size <= 1:
            return True
        diffs = np.diff(ones) - 1
        return k <= np.min(diffs)
