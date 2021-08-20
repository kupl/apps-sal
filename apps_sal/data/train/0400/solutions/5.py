class Solution:

    def largestRectangleArea(self, heights):
        n = len(heights)
        if n == 0:
            return 0
        left = [i for i in range(n)]
        right = [i + 1 for i in range(n)]
        print(heights)
        for i in range(1, n):
            cur = i - 1
            while cur >= 0 and heights[cur] >= heights[i]:
                left[i] = left[cur]
                cur = left[cur] - 1
        for j in range(n - 1, -1, -1):
            cur = j + 1
            while cur < n and heights[cur] >= heights[j]:
                right[j] = right[cur]
                cur = right[cur]
        print(left)
        print(right)
        max_val = 0
        for i in range(n):
            tmp = heights[i] * (right[i] - left[i])
            if max_val < tmp:
                max_val = tmp
        return max_val
