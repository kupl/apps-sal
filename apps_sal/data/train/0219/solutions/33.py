class Solution:
    def longestWPI(self, h: List[int]) -> int:
        n = len(h)
        for i in range(n):
            if h[i] > 8:
                h[i] = 1
            else:
                h[i] = -1
        pre = [0] * n
        pre[0] = h[0]
        maxi = 0
        for i in range(1, n):
            pre[i] = pre[i - 1] + h[i]
        d = {}
        print(pre)
        for x in range(n):
            if pre[x] > 0:
                maxi = x + 1
            if d.get(pre[x] - 1, -1) != -1:
                maxi = max(maxi, x - d[pre[x] - 1])
            if d.get(pre[x], -1) == -1:
                d[pre[x]] = x
        return maxi
