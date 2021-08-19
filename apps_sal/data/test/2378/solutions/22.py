import sys
sys.setrecursionlimit(10 ** 7)
P = 10 ** 9 + 7
N = int(input())
edges = [[] for i in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    edges[a - 1].append((b - 1, i))
    edges[b - 1].append((a - 1, i))
L = [0 for i in range(N)]


def dfs(cur, x):
    res = 1
    for i in edges[cur]:
        if i[1] != x:
            res += dfs(i[0], i[1])
    L[x] = res
    return res


dfs(0, -1)
L2 = [1]
i2 = pow(2, P - 2, P)
for i in range(N):
    L2.append(L2[-1] * i2 % P)
cnt = 0
for i in L:
    cnt += (1 - L2[i]) * (1 - L2[N - i])
print((-N * i2 - L2[-1] + cnt + 1) % P)
