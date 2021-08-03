class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # fix i and test for j

        # count arr1 i, arr2 i, ind
        minmin = []
        minmax = []
        maxmin = []
        maxmax = []
        res = 0
        for i, (v1, v2) in enumerate(zip(arr1, arr2)):

            if not minmin or minmin[0] - v1 + minmin[1] - v2 + minmin[2] - i > 0:
                minmin = [v1, v2, i]
            if not minmax or minmax[0] - v1 + v2 - minmax[1] + minmax[2] - i > 0:
                minmax = [v1, v2, i]

            if not maxmin or v1 - maxmin[0] + maxmin[1] - v2 + maxmin[2] - i > 0:
                maxmin = [v1, v2, i]

            if not maxmax or v1 - maxmax[0] + v2 - maxmax[1] + maxmax[2] - i > 0:
                maxmax = [v1, v2, i]
            res = max(res, v1 - minmin[0] + v2 - minmin[1] + i - minmin[2])
            res = max(res, v1 - minmax[0] + minmax[1] - v2 + i - minmax[2])
            res = max(res, maxmin[0] - v1 + v2 - maxmin[1] + i - maxmin[2])
            res = max(res, maxmax[0] - v1 + maxmax[1] - v2 + i - maxmax[2])
            # print(maxmax[0]-v1+maxmax[1]-v2+i-maxmin[2])
        # print(minmin,minmax,maxmin,maxmax)
        return res
