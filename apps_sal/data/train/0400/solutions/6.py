class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights:
            return 0
        N = len(heights)
        left, right = [1] * N, [1] * N
        for i in range(1, N):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                left[i] += left[j]
                j -= left[j]
        for i in range(N - 1, -1, -1):
            j = i + 1
            while j <= N - 1 and heights[j] >= heights[i]:
                right[i] += right[j]
                j += right[j]
        return max((l + r - 1) * h for l, r, h in zip(left, right, heights))
