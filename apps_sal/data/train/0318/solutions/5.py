class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3
        def linear(arr):
            # index = nb slices eaten.
            a = [0] * (n+1)  # Two slices ago.
            b = [0] * (n+1)  # Previous slice.
            for x in arr:
                a, b = b, [i and max(x + a[i-1], b[i]) for i in range(n+1)]
                # print(a,b)
            return b[-1]
        return max(linear(slices[1:]), linear(slices[:-1]))

