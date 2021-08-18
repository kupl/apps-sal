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

改行あり整数
x = []
y = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

N行M列の初期化
dp = [[INF] * M for i in range(N)]

'''

N, M = list(map(int, input().split()))
S = input()


now = N
ans = []
while now > 0:
    for step in range(M, 0, -1):
        if now - step < 0:
            step = now
        if S[now - step] == "0":
            ans.append(step)
            now -= step
            break
        if step == 1:
            print((-1))
            return

ans.reverse()
ret = ""
for a in ans:
    ret += str(a) + " "

print(ret)
