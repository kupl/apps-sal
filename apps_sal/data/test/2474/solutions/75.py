import sys
import math
import fractions
import bisect
import queue
import heapq
from collections import deque
sys.setrecursionlimit(4100000)

MOD = int(1e9 + 7)
PI = 3.14159265358979323846264338327950288
INF = 1e18

'''
1行のint
N, K = map(int, input().split())

1行のstring
S, T = input().split()

1行の整数配列
P = list(map(int,input().split()))

改行あり
x = []
y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

N行M列の初期化
dp = [[INF] * M for i in range(N)]

'''


N = int(input())
C = list(map(int, input().split()))

C.sort()

beki = [1]
for i in range(1, 3 * N + 20):
    beki.append((beki[i - 1] * 2) % MOD)


ans = 0
for i in range(N):
    ans += (C[i] * beki[2 * N - 2] * (N - i + 1)) % MOD


print((ans % MOD))
