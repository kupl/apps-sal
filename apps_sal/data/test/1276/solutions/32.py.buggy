import collections
import sys
import math
sys.setrecursionlimit(10 ** 7)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]


N = INT()
S = input()
if N < 3:
    print(0)
    return
r = S.count("R")
g = S.count("G")
b = S.count("B")
ans = r * g * b
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = j * 2 - i
        if k >= N:
            continue
        if S[j] != S[i] and S[k] != S[i] and S[j] != S[k]:
            ans -= 1
print(ans)
