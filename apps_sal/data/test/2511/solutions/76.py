import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, k = map(int, input().split())
ab = [[]for _ in range(n)]
visited = [False] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)
ans = k


def dfs(i):
    nonlocal ans
    child = 0
    visited[i] = True
    for x in ab[i]:
        if visited[x] == False:
            dfs(x)
            child += 1
    if i == 0:
        ans *= p(k - 1, child)
    else:
        ans *= p(k - 2, child)
    ans %= mod


def p(a, b):
    e = 1
    for i in range(a, a - b, -1):
        e *= i
        e %= mod
    return e


mod = 10**9 + 7
dfs(0)
print(ans)
