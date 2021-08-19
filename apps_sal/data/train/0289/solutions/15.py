class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        dl = {}
        dm = {}
        if M > L:
            (M, L) = (L, M)
        ls = sum(A[0:L])
        ms = sum(A[0:M])
        dl[0, L - 1] = ls
        dm[0, M - 1] = ms
        c = 0
        while c + L < len(A):
            ls -= A[c]
            ls += A[L + c]
            dl[0 + c + 1, L + c] = ls
            c += 1
        c = 0
        while c + M < len(A):
            ms -= A[c]
            ms += A[M + c]
            dm[0 + c + 1, M + c] = ms
            c += 1
        dll = sorted(list(dl.items()), key=lambda x: x[1], reverse=True)
        mll = sorted(list(dm.items()), key=lambda x: x[1], reverse=True)
        f = -1
        for x in dll:
            lower = x[0][0]
            upper = x[0][1]
            val = x[1]
            for y in mll:
                ly = y[0][0]
                uy = y[0][1]
                yval = y[1]
                if lower <= ly <= upper or lower <= uy <= upper:
                    continue
                maxVal = yval + val
                if maxVal == 125:
                    print(lower, upper, ly, uy)
                    print(x, y)
                f = max(maxVal, f)
        return f
