from queue import PriorityQueue
import sys

sys.setrecursionlimit(10**9)


def IA(): return [int(x) for x in input().split()]
def IM(N): return [IA() for _ in range(N)]


N = 100005
fa = [int(0) for i in range(2 * (N + 1))]
xNum = [int(0) for i in range(2 * (N + 1))]
yNum = [int(0) for i in range(2 * (N + 1))]


def find(x):
    if(x == fa[x]):
        return x
    else:
        fa[x] = find(fa[x])
        return fa[x]


n = input()
n = int(n)

for i in range(2 * N + 1):
    fa[i] = i

for i in range(n):
    x, y = IA()
    y += N
    fx = int(find(x))
    fy = int(find(y))

    if(fx != fy):
        fa[fy] = fx
for i in range(N):
    xNum[find(i)] += 1
for i in range(N):
    yNum[find(i + N)] += 1
ans = 0
for i in range(N):
    ans += xNum[i] * yNum[i]
print((ans - n))
