import bisect
import itertools
import numpy as np

def search_cut(N, M, A):
    high_cut = A[-1] * 2
    low_cut = A[0] * 2

    while high_cut > low_cut + 1:
        mid = (high_cut + low_cut) // 2
        count = (N  - np.searchsorted(A, mid - A, side = 'left')).sum()

        if count > M:
            low_cut = mid
        else:
            high_cut = mid

    return low_cut, high_cut

def happiness(N, M, A, low_cut, high_cut):
    A_sum = np.zeros(N + 1)
    A_sum[1:] = np.cumsum(A)
    X = np.searchsorted(A, high_cut - A, side = 'left')
    happiness = (A_sum[-1] - A_sum[X]).sum()
    happiness += ((N - X) * A).sum()
    happiness += (M - (N - X).sum()) * low_cut

    return int(happiness)


N, M = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
A = np.sort(A)

low_cut, high_cut = search_cut(N, M, A)
ans = happiness(N, M, A, low_cut, high_cut)
print(ans)

