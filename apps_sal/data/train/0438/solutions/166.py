class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        size = len(arr)
        if m == size:
            return m
        (length, ans) = ([0] * (len(arr) + 2), -1)
        for (i, n) in enumerate(arr):
            (left, right) = (length[n - 1], length[n + 1])
            if left == m or right == m:
                ans = i
            length[n - left] = length[n + right] = left + right + 1
        return ans
