class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # # sol1: mono_inc stack
        # stack = [(-1, 0)]
        # res = 0
        # for i, h in enumerate(heights + [0]):
        #     while stack[-1][1] > h:
        #         H = stack.pop()[1]
        #         W = i - stack[-1][0] - 1
        #         res = max(res, H*W)
        #     stack.append((i, h))
        # return res

        # sol2: left/right(include self) higher neighbors
        if not heights:
            return 0
        N = len(heights)
        left, right = [1] * N, [1] * N
        for i in range(1, N):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                left[i] += left[j]
                j -= left[j]
        for i in range(N - 1, -1, -1):  # 注意降序要写完整 -1, -1
            j = i + 1
            while j <= N - 1 and heights[j] >= heights[i]:
                right[i] += right[j]
                j += right[j]
        return max((l + r - 1) * h for l, r, h in zip(left, right, heights))
