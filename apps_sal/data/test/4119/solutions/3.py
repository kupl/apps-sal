from itertools import accumulate
import sys


def LI():
    return list(map(int, input().split()))


N, M = LI()
X = LI()
if M <= N:
    print((0))
    return
sa = []
X.sort()
for i in range(M-1):
    sa.append(X[i+1]-X[i])
sa.sort(reverse=True)
sa = list(accumulate(sa))
if N == 1:
    print((sa[M-2]))
else:
    print((sa[M-2]-sa[N-2]))

