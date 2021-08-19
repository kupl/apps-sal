class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        n = len(horizontalCuts)
        m = len(verticalCuts)
        A = horizontalCuts[:]
        B = verticalCuts[:]
        A.sort()
        B.sort()
        A.insert(0, 0)
        B.insert(0, 0)
        A.append(h)
        B.append(w)
        maxw = 0
        maxh = 0
        for i in range(1, n + 2):
            maxh = max(maxh, A[i] - A[i - 1])
        for i in range(1, m + 2):
            maxw = max(maxw, B[i] - B[i - 1])
        m = 10 ** 9 + 7
        return maxw % m * (maxh % m) % m
