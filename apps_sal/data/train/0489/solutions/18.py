class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        arr = sorted([(a, i) for i, a in enumerate(A)])
        rindex = [0] * n
        rindex[-1] = arr[-1][1]
        for i in range(n - 2, -1, -1):
            rindex[i] = max(arr[i][1], rindex[i + 1])
        mx = 0
        for i in range(n):
            mx = max(mx, rindex[i] - arr[i][1])
        return mx
