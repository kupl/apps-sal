import bisect
import numpy as np

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


def simple():
    B = sorted([A[i] * A[j] for i in range(N) for j in range(i + 1, N)])
    return B[K - 1]


def solve():
    A.sort()

    iplus = bisect.bisect_right(A, 0)
    izeros = bisect.bisect_left(A, 0)

    pluss = np.array(A[iplus:]).astype(np.int64)
    zeros = A[izeros:iplus]
    minuss = np.array(A[:izeros]).astype(np.int64)

    nplus = len(pluss)
    nzero = len(zeros)
    nminus = len(minuss)

    npminus = nplus * nminus
    npzeros = nzero * (nplus + nminus) + nzero * (nzero - 1) // 2

    if npminus < K <= npminus + npzeros:
        return 0
    elif K <= npminus:
        mn = A[-1] * A[0] - 1
        mx = 0
        while mx - mn > 1:
            mid = (mn + mx) // 2
            xs = -(-mid // minuss)
            cnt = nplus * nminus
            cnt -= np.sum(np.searchsorted(pluss, xs, side="left"))
            if cnt >= K:
                mx = mid
            else:
                mn = mid
        return mx
    else:
        nK = K - npminus - npzeros
        pluss2 = (-minuss)[::-1]
        mn = -1
        mx = max(A[0]**2, A[-1]**2)
        pluss_p2 = pluss**2
        pluss2_p2 = pluss2**2
        while mx - mn > 1:
            mid = (mn + mx) // 2
            cnt = 0
            xs = mid // pluss
            cnt += np.sum(np.searchsorted(pluss, xs, side='right'))
            cnt -= np.count_nonzero(pluss_p2 <= mid)
            xs2 = mid // pluss2
            cnt += np.sum(np.searchsorted(pluss2, xs2, side='right'))
            cnt -= np.count_nonzero(pluss2_p2 <= mid)
            cnt = cnt // 2
            if nK <= cnt:
                mx = mid
            else:
                mn = mid
        return mx


print((solve()))
