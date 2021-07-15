class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        H = [0] + horizontalCuts + [h]
        W = [0] + verticalCuts + [w]
        H.sort()
        W.sort()

        hmax, wmax = 0, 0
        for i in range(1, len(H)):
            hmax = max(hmax, H[i] - H[i - 1])

        for i in range(1, len(W)):
            wmax = max(wmax, W[i] - W[i - 1])

        return hmax * wmax % 1000000007
