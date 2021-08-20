class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        record = [[A[i], i] for i in range(len(A))]
        record.sort(key=lambda x: [x[0], x[1]])
        res = 0
        pre_min = record[0][1]
        for i in range(1, len(A)):
            pre_min = min(pre_min, record[i][1])
            res = max(res, record[i][1] - pre_min)
        return res
