class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        length = [0 for _ in range(n + 2)]
        res = -1
        for (step, pos) in enumerate(arr):
            (left, right) = (length[pos - 1], length[pos + 1])
            if left == m or right == m:
                res = step
            length[pos - left] = length[pos + right] = left + right + 1
        return res
