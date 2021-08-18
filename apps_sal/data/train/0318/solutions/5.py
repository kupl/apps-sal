class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        def linear(arr):
            a = [0] * (n + 1)
            b = [0] * (n + 1)
            for x in arr:
                a, b = b, [i and max(x + a[i - 1], b[i]) for i in range(n + 1)]
            return b[-1]
        return max(linear(slices[1:]), linear(slices[:-1]))
