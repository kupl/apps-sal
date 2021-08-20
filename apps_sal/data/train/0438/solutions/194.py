class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        length = [0 for _ in range(len(arr) + 2)]
        res = -1
        for (i, n) in enumerate(arr):
            (left, right) = (length[n - 1], length[n + 1])
            if left == m or right == m:
                res = i
            length[n - left] = length[n + right] = left + right + 1
        return res
