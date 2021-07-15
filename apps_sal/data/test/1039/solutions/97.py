import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
d = [-1 for i in range(n)]
e = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    e[a - 1].append([b - 1, c])
    e[b - 1].append([a - 1, c])
q, k = map(int, input().split())
def dfs(cur, par, di):
    d[cur] = di
    for i in e[cur]:
        if d[i[0]] == -1:
            if i == par:
                continue
            dfs(i[0], cur, di + i[1])
dfs(k - 1, -1, 0)
for i in range(q):
    x, y = map(int, input().split())
    print(d[x - 1] + d[y - 1])
