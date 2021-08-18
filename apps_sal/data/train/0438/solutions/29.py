class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m

        lengths = [0] * (len(arr) + 2)

        ans = -1

        for (step, value) in enumerate(arr):
            left, right = lengths[value - 1], lengths[value + 1]

            if left == m or right == m:
                ans = step

            lengths[value - left] = lengths[value + right] = left + right + 1

        return ans
