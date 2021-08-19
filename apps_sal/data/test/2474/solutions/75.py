import sys
import math
import fractions
import bisect
import queue
import heapq
from collections import deque
sys.setrecursionlimit(4100000)
MOD = int(1000000000.0 + 7)
PI = 3.141592653589793
INF = 1e+18
'\n1行のint\nN, K = map(int, input().split())\n\n1行のstring\nS, T = input().split()\n\n1行の整数配列\nP = list(map(int,input().split()))\n\n改行あり\nx = []\ny = []\nfor i in range(N):\n    x1,y1=[int(i) for i in input().split()]\n    x.append(x1)\n    y.append(y1)\n\nN行M列の初期化\ndp = [[INF] * M for i in range(N)]\n\n'
N = int(input())
C = list(map(int, input().split()))
C.sort()
beki = [1]
for i in range(1, 3 * N + 20):
    beki.append(beki[i - 1] * 2 % MOD)
ans = 0
for i in range(N):
    ans += C[i] * beki[2 * N - 2] * (N - i + 1) % MOD
print(ans % MOD)
