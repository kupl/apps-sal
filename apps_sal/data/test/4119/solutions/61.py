# author:  Taichicchi
# created: 10.10.2020 19:46:14

import sys

N, M = list(map(int, input().split()))

if M < N:
    print((0))
    return

X = list(map(int, input().split()))

X.sort()


ls = []
for i in range(M - 1):
    ls.append(X[i + 1] - X[i])


ls.sort(reverse=True)

print((X[M - 1] - X[0] - sum(ls[:N - 1])))

