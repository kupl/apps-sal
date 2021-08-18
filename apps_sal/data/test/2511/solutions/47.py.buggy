import sys
sys.setrecursionlimit(500000)

N, K = map(int, input().split())

T = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    T[a - 1].append(b - 1)
    T[b - 1].append(a - 1)

ans = 1


def dfs(i, bb, b, p):
    nonlocal ans
    ans = (ans * (K - bb - b)) % (10**9 + 7)
    cnt = 0
    for j in T[i]:
        if j == p:
            continue
        dfs(j, b + cnt, 1, i)
        cnt += 1


dfs(0, 0, 0, -1)
print(ans)
