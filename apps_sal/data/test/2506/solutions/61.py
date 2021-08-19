import sys
import math
import fractions
from collections import defaultdict
import bisect
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


(N, M) = nm()
A = nl()
A.sort()
S = [0]
S[0] = A[0]
for i in range(1, N):
    S.append(S[i - 1] + A[i])


def clc_shake(x):
    tot = 0
    for i in range(N):
        th = x - A[i]
        inds = bisect.bisect_left(A, th)
        tot += N - inds
    return tot


l = 0
r = 2 * 10 ** 6
c = 0
while l + 1 < r:
    c = (l + r) // 2
    if clc_shake(c) < M:
        r = c
    else:
        l = c
ans = 0
for i in range(N):
    th = r - A[i]
    inds = bisect.bisect_left(A, th)
    if inds != 0:
        ans += (N - inds) * A[i] + (S[N - 1] - S[inds - 1])
    else:
        ans += (N - inds) * A[i] + S[N - 1]
M2 = M - clc_shake(r)
ans += M2 * l
print(ans)
