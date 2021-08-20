class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M > len(A):
            assert False
        l = []
        s = 0
        for i in range(len(A) - L + 1):
            if i == 0:
                s = sum(A[:L])
            else:
                s -= A[i - 1]
                s += A[i + L - 1]
            l.append((-s, (i, i + L - 1)))
        l = sorted(l, key=lambda tup: tup[0])
        m = []
        s = 0
        for i in range(len(A) - M + 1):
            if i == 0:
                s = sum(A[:M])
            else:
                s -= A[i - 1]
                s += A[i + M - 1]
            m.append((-s, (i, i + M - 1)))
        m = sorted(m, key=lambda tup: tup[0])
        maximum = 0
        for i in range(len(l)):
            for j in range(len(m)):
                (sl, (il, jl)) = l[i]
                (sm, (im, jm)) = m[j]
                (sl, sm) = (-sl, -sm)
                if sl + sm > maximum:
                    if jl < im or jm < il:
                        maximum = sl + sm
                else:
                    break
        return maximum
