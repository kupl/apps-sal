n = int(input())
p = list(map(int, input().split()))
p = [i - 1 for i in p]
vis = [False for _ in range(n)]

sz = [0]


def dfs(v):
    cnt = 0
    while not vis[v]:
        vis[v] = True
        cnt += 1
        v = p[v]
    return cnt


for i in range(n):
    cnt = dfs(i)
    if cnt > 0:
        sz.append(cnt)

sz.sort()
print(sum(list(map(lambda x: x * x, sz))) + 2 * sz[-1] * sz[-2])
