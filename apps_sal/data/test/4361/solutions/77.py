from sys import stdin
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


n, k = readInts()
A = [I() for _ in range(n)]
A = sorted(A)
a = INF
for i in range(n - k + 1):
    a = min(a, abs(A[i + k - 1] - A[i]))
print(a)
