from bisect import bisect_left
import sys
inf = float('inf')
mod = 1000000007


def array():
    return list(map(int, sys.stdin.readline().split()))


def intt():
    return list(map(int, sys.stdin.readline().split()))


(n, m, k) = list(map(int, sys.stdin.readline().split()))
ls = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    ls.append(arr)
print(m * (m - 1) // 2)
for i in range(1, m):
    for j in range(i + 1, m + 1):
        if k == 0:
            print(i, j)
        else:
            print(j, i)
