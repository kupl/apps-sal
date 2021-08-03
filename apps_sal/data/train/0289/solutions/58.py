class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        Lsum = [(sum(A[:L]), 0)]
        Msum = [(sum(A[:M]), 0)]
        for i in range(1, len(A) - L + 1):
            Lsum.append((Lsum[-1][0] - A[i - 1] + A[i + L - 1], i))
        for i in range(1, len(A) - M + 1):
            Msum.append((Msum[-1][0] - A[i - 1] + A[i + M - 1], i))
        Lsum.sort(reverse=True)
        Msum.sort(reverse=True)
        ret = sum(A[:L + M])
        for li in range(len(Lsum)):
            breakFlag = True
            for mi in range(len(Msum)):
                if (Lsum[li][1] <= Msum[mi][1] and Lsum[li][1] + L > Msum[mi][1]) or (Msum[mi][1] <= Lsum[li][1] and Msum[mi][1] + M > Lsum[li][1]):
                    breakFlag = False
                    continue
                ret = max(ret, Lsum[li][0] + Msum[mi][0])
                break
            if breakFlag:
                break
        return ret
