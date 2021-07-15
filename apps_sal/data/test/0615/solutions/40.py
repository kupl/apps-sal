from bisect import bisect_right, bisect_left
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A = [0] + A
a = list(accumulate(A))
answer = a[-1]

# 切り口はN-1個, 真ん中の選び方はN-3
for i in range(N - 3):
    left = a[i + 2]
    right = a[-1] - left
    p = bisect_left(a, left // 2)
    P1 = a[p]
    Q1 = left - P1
    P2 = a[p - 1]
    Q2 = left - P2
    if abs(P1 - Q1) <= abs(P2 - Q2):
        P = P1
        Q = Q1
    else:
        P = P2
        Q = Q2

    s = bisect_right(a, a[-1] - right // 2)
    S1 = a[-1] - a[s - 1]
    R1 = right - S1
    S2 = a[-1] - a[s]
    R2 = right - S2
    if abs(S1 - R1) <= abs(S2 - R2):
        S = S1
        R = R1
    else:
        S = S2
        R = R2

    answer = min(answer, max(P, Q, R, S) - min(P, Q, R, S))

print(answer)
