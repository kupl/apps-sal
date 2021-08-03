import sys


def input():
    return sys.stdin.readline()[:-1]


def make_sumtable():
    sumtable = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        sumtable[L[i]][R[i]] += 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            sumtable[i][j] += sumtable[i - 1][j]
            sumtable[i][j] += sumtable[i][j - 1]
            sumtable[i][j] -= sumtable[i - 1][j - 1]
    return sumtable


N, M, Q = list(map(int, input().split()))

L = []
R = []
for i in range(M):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

sumtable = make_sumtable()

for i in range(Q):
    p, q = list(map(int, input().split()))
    print((sumtable[q][q] - sumtable[q][p - 1] - sumtable[p - 1][q] + sumtable[p - 1][p - 1]))
