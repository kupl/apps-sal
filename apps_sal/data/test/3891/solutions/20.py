import sys
from itertools import permutations
DEBUG = 0
if DEBUG:
    f = open('input.txt', 'r')
    input = f.readline
else:
    input = sys.stdin.readline


def mp():
    return list(map(int, input().split()))


def main():
    INF = int(1000000000.0)
    (n, m) = mp()
    a = []
    for i in range(n):
        a.append(input().strip())
    (imax, imin, jmax, jmin) = (0, INF, 0, INF)
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'B':
                imax = max(imax, i)
                jmax = max(jmax, j)
                jmin = min(jmin, j)
                imin = min(imin, i)
    print((imax + imin) // 2 + 1, 1 + (jmax + jmin) // 2)


main()
