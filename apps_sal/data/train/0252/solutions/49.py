class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_right = [0] * (n + 1)

        for i, x in enumerate(ranges):
            max_right[max(0, i - x)] = max(max_right[max(0, i - x)], i + x)

        i = 0
        best_right = 0
        ans = 0
        j = 0

        while i < n:
            while j <= i:
                best_right = max(max_right[j], best_right)
                j += 1

            if best_right <= i:
                return -1

            ans += 1
            i = best_right

        return ans
