import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N=II()
AB = [LI() for _ in range(N-1)]

graph = [[] for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]: continue
        parent[y] = x
        stack.append(y)

x = (DVSR + 1) // 2
PWR=[1]*(N+1)
RWP=[1]*(N+1)

for i in range(1,N+1):
    PWR[i] = PWR[i-1] * 2 % DVSR
    RWP[i] = RWP[i-1] * x % DVSR

answer = 0
size = [1] * (N+1)
for v in order[::-1]:
    p = parent[v]
    size[p] += size[v]
    A = [size[w] for w in graph[v] if w != p]
    if v != root: A.append(N - 1 - sum(A))
    if len(A) == 1: continue
    prod = 1
    coef = 1
    for x in A:
        prod *= RWP[x]
        prod %= DVSR
        coef += (PWR[x] - 1)
    E = 1 - prod * coef % DVSR
    answer += E

answer *= RWP[1]
answer %= DVSR
print(answer)
