class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        helper = []
        for (i, x) in enumerate(A):
            helper.append((x, i))
        helper.sort(key=lambda x: x[0])
        imin = helper[0][1]
        maxlen = 0
        for (val, indx) in helper:
            if indx >= imin:
                maxlen = max(maxlen, indx - imin)
            imin = min(imin, indx)
        return maxlen
