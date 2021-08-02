from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(n - 1):
    u, v, x = list(map(int, input().split()))
    u, v = u - 1, v - 1
    if not x:
        g[u].append(v)
        g[v].append(u)
MOD = 10**9 + 7

res = pow(n, k, MOD)

visited = [False for _ in range(n)]
for i in range(n):
    if not visited[i]:
        cnt = 1
        visited[i] = True
        stack = [i]
        while stack:
            curr = stack.pop()
            for ne in g[curr]:
                if not visited[ne]:
                    visited[ne] = True
                    cnt += 1
                    stack.append(ne)
        res -= pow(cnt, k, MOD)

print(res % MOD)
