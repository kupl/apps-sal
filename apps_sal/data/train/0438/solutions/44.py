
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        length = [0] * (n + 2)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            if left == m or right == m:
                res = i
            length[a - left] = length[a + right] = left + right + 1
        return res
