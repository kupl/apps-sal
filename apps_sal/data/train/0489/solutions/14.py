class Solution:

    def maxWidthRamp(self, A):
        sorted_idx = [x[0] for x in sorted(enumerate(A), key=lambda x: x[1])]
        res = 0
        min_idx = sorted_idx[0]
        for idx in sorted_idx:
            res = max(res, idx - min_idx)
            min_idx = min(min_idx, idx)
        return res
