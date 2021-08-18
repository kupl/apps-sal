import numpy as np
N, K = map(int, input().split())
A = np.array(tuple(map(int, input().split())))
F = np.array(tuple(map(int, input().split())))

if sum(A) <= K:
    print(0)
else:
    def solve(N, K, A, F):
        A = np.sort(A)
        F = np.sort(F)[::-1]
        l = -1
        r = 10**12
        while (r - l) > 1:
            mid = (r + l) // 2
            fmid = (np.fmax([0] * N, A - (mid // F))).sum()
            if fmid <= K:
                r = mid
            else:
                l = mid
        return(r)
    print(solve(N, K, A, F))
