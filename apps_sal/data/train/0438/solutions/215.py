class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        lengths = [0] * (len(arr) + 2)
        result = -1
        for i, a in enumerate(arr):
            left, right = lengths[a - 1], lengths[a + 1]
            if left == m or right == m:
                result = i
            lengths[a - left] = lengths[a + right] = left + right + 1
        return result
            

