class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr or k == 0:
            return 0
        N = 10 ** 9 + 7
        n = len(arr)
        accu = [0] * (n + 1)
        for i in range(1, n + 1):
            accu[i] = accu[i - 1] + arr[i - 1]
        s = accu[-1]
        accuMaxL = max(accu)
        accuMaxR = s - min(accu)
        (a0, sMax) = (0, 0)
        for a in accu:
            a0 = min(a, a0)
            sMax = max(sMax, a - a0)
        if sMax <= 0:
            return 0
        elif k == 1:
            return sMax
        elif s <= 0:
            ans = max(sMax, accuMaxR + accuMaxL)
            return ans
        elif (sMax - accuMaxL - accuMaxR) / k > s:
            return sMax
        else:
            ans = accuMaxR + accuMaxL % N
            for i in range(k - 2):
                ans = (ans + s) % N
            return ans
