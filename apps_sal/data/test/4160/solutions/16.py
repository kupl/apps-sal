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


X = I()
m = 100
cnt = 0
while m < X:
    m += m // 100
    cnt += 1
print(cnt)
