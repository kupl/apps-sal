from itertools import accumulate
from bisect import bisect_left
N = int(input())
A = [0] + list(map(int, input().split()))


ans = float('inf')
A = list(accumulate(A))

for m in range(2, N - 1):
    Lx = A[m] // 2
    Li = bisect_left(A, Lx)
    if abs(Lx - A[Li]) > abs(Lx - A[Li - 1]):
        Li -= 1

    Rx = (A[-1] + A[m]) // 2
    Ri = bisect_left(A, Rx)
    if abs(Rx - A[Ri]) > abs(Rx - A[Ri - 1]):
        Ri -= 1

    P, Q, R, S = A[Li], A[m] - A[Li], A[Ri] - A[m], A[-1] - A[Ri]
    tmp_ans = max(P, Q, R, S) - min(P, Q, R, S)
    ans = min(ans, tmp_ans)


print(ans)
