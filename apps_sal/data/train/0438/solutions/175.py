class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        res = -1
        ln = [0] * (len(arr) + 2)

        for i, a in enumerate(arr):
            left, right = ln[a - 1], ln[a + 1]
            if left == m or right == m:
                res = i
            ln[a - left] = ln[a + right] = left + right + 1

        return res
