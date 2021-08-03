# http://codeforces.com/problemset/problem/486/E
import sys
import re
import collections
import threading
import bisect  # bisect.bisect(list, value)

N = 0

Last = []
AA = [0 for _ in range(100005)]
LL = [0 for _ in range(100005)]
BB = [0 for _ in range(100005)]  # reverse
SS = [0 for _ in range(100005)]  # reverse
TT = [0 for _ in range(100005)]  # reverse
ANS = [1 for _ in range(100005)]


def LIS(A, L):
    nonlocal N

    Last.append(-1)  # dummy

    for i in range(N):
        if Last[-1] < A[i]:
            Last.append(A[i])

        it = bisect.bisect_left(Last, A[i])  # lower_bound() in C++

        Last[it] = A[i]
        L[i] = it


N = int(sys.stdin.readline())
AA = list(map(int, sys.stdin.readline().strip().split()))

LIS(AA, LL)

length = max(LL)

for i in range(N):
    BB[N - i - 1] = 1000000 - AA[i]

Last = []

LIS(BB, SS)

for i in range(N):
    TT[N - i - 1] = SS[i]

for i in range(N):
    if LL[i] + TT[i] == length + 1:
        ANS[i] = 3

maxi = 0
mini = 1000000

for i in range(N):
    if ANS[i] != 1:
        if AA[i] <= maxi:
            ANS[i] = 2
        maxi = max(maxi, AA[i])

for i in range(N - 1, -1, -1):
    if ANS[i] != 1:
        if AA[i] >= mini:
            ANS[i] = 2
        mini = min(mini, AA[i])

for i in range(N):
    print(ANS[i], end="", flush=True)

print()
