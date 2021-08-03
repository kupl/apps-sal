class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        H = {0: -1}
        total = 0
        M = len(arr) + 1

        for i, a in enumerate(arr):
            total += a
            H[total] = i

        result = M
        minL = M
        total = 0
        for i, a in enumerate(arr):
            total += a

            if total - target in H:
                minL = min(minL, i - H[total - target])

            if total + target in H and minL < M:
                result = min(result, minL + H[total + target] - i)

        return result if result < M else -1
