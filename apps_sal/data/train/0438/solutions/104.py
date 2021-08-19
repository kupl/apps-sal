class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        counts = [0] * (len(arr) + 2)
        ans = -1
        for (index, i) in enumerate(arr):
            left = counts[i - 1]
            right = counts[i + 1]
            total = 1 + left + right
            counts[i] = total
            counts[i - left] = total
            counts[i + right] = total
            if left == m or right == m:
                ans = index
        return ans
