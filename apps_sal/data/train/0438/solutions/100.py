class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        length = [0] * (len(arr) + 2)
        res = -1
        for (i, v) in enumerate(arr):
            (left, right) = (length[v - 1], length[v + 1])
            if left == m or right == m:
                res = i
            length[v - left] = length[v + right] = left + right + 1
        return res
