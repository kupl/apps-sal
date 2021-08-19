import numpy as np


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] > 0 else 0
        St = [i for (i, j) in enumerate(nums) if i == 0 and j != 0 or (nums[i - 1] == 0 and j != 0)]
        if len(St) == 0:
            return 0
        Ed = [i for (i, j) in enumerate(nums) if i == len(nums) - 1 and j != 0 or (i < len(nums) - 1 and nums[i + 1] == 0 and (j != 0))]
        Sta = np.array(St)
        Eda = np.array(Ed)
        Lns = (-(Eda - Sta + 1)).argsort()
        k = 0
        mxLen = 0
        while k < len(Lns):
            nums1 = nums[St[Lns[k]]:Ed[Lns[k]] + 1]
            if len(nums1) == mxLen:
                return mxLen
            ni = [i for (i, j) in enumerate(nums1) if j < 0]
            if len(ni) == 0 or len(ni) % 2 == 0:
                mxLen = max(mxLen, len(nums1))
            else:
                mn = min(ni)
                mx = max(ni)
                mxLen = max(mxLen, mn, len(nums1) - mn - 1, mx, len(nums1) - mx - 1)
            k = k + 1
        return mxLen
