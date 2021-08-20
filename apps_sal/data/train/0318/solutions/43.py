class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        if n == 1:
            return max(slices)

        @lru_cache(None)
        def process(f, p, i, k):
            if i == 0:
                return slices[0] if f == 1 else 0
            if p == 1:
                return process(f, 0, i - 1, k)
            elif i == 1 and f == 1 or k == 0:
                return process(f, 0, i - 1, k)
            else:
                return max(process(f, 0, i - 1, k), slices[i] + process(f, 1, i - 1, k - 1))
        return max(process(0, 0, 3 * n - 1, n), process(1, 1, 3 * n - 1, n - 1))
