from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i in range(len(AL[v][CHILDREN])):
        u = AL[v][CHILDREN][i]
        if visited[u]:
            AL[v][CHILDREN][i] = None
            continue
        AL[v][SIZE] += dfs(u)
    return AL[v][SIZE]


def anaaki(v):
    ret = powp - 1
    for ch in AL[v][CHILDREN]:
        if ch is None:
            continue
        ret -= pow(2, AL[ch][SIZE], p) - 1
        ret %= p
    ret -= pow(2, n - AL[v][SIZE], p) - 1
    ret %= p
    return ret


n = int(input())
SIZE = 0
CHILDREN = 1
AL = [[1, []] for _ in range(n)]
visited = [False] * n
p = 10 ** 9 + 7
powp = pow(2, n - 1, p)

for i in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    AL[a][CHILDREN].append(b)
    AL[b][CHILDREN].append(a)

dfs(0)
numer = 0
for i in range(n):
    numer += anaaki(i)
    numer %= p

denom = pow(2, n, p)
print(numer * pow(denom, p - 2, p) % p)
