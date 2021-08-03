class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        res = -1
        length = [0 for _ in range(n + 2)]

        for i, val in enumerate(arr):
            left, right = length[val - 1], length[val + 1]
            if left == m or right == m:
                res = i
            length[val - left] = length[val + right] = left + right + 1
        return res
