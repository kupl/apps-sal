import sys
sys.setrecursionlimit(10 ** 7)
mod = 10 ** 9 + 7
n = int(input())
edges = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append((b - 1, i))
    edges[b - 1].append((a - 1, i))
l = [0 for i in range(n)]
def dfs(cur, x):
    res = 1
    for i in edges[cur]:
        if i[1] != x:
            res += dfs(i[0], i[1])
    l[x] = res
    return res
dfs(0, -1)
l2 = [1]
i2 = pow(2, mod - 2, mod)
for i in range(n):
    l2.append(l2[-1] * i2 % mod)
cnt = 0
for i in l:
    cnt += (1 - l2[i]) * (1 - l2[n - i])
print((-n * i2 - l2[-1] + cnt + 1) % mod)
