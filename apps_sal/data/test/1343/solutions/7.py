import sys
from decimal import *


def main():

    n, m, k = list(map(int, sys.stdin.readline().split()))

    e = [[] for i in range(n)]
    sk = [False for i in range(n)]

    for i in range(m):
        u, v, l = list(map(int, sys.stdin.readline().split()))
        u = u - 1
        v = v - 1
        e[u].append((v, l))
        e[v].append((u, l))

    if k > 0:
        x = list(map(int, sys.stdin.readline().split()))
        for i in x:
            sk[i - 1] = True

    best = None
    for i in range(n):
        if sk[i]:
            continue
        for j in range(len(e[i])):
            a, l = e[i][j]
            if sk[a]:
                if best is None:
                    best = l
                elif best > l:
                    best = l
    if best is None:
        print(-1)
    else:
        print(best)


main()
