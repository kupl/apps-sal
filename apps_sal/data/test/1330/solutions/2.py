import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
d = int(input())
disable = [False] * n
base = 5001
ds = [int(input()) - 1 for _ in range(d)]
for ele in ds:
    disable[ele] = True


childs = [[] for i in range(base + m + 1)]

for idx, (i, j) in enumerate(zip(p, c)):
    if not disable[idx]:
        childs[i].append(base + j)


vis = [False] * (base + m + 1)
matching = [-1] * (base + m + 1)


def dfs(num):
    for child in childs[num]:
        if not vis[child]:
            vis[child] = True
            if matching[child] == -1 or dfs(matching[child]):
                matching[child] = num
                return True
    return False


ans = []
mex = 0
for idx in range(d - 1, -1, -1):
    while True:
        vis = [False] * (base + m + 1)
        if not dfs(mex):
            break
        mex += 1
    ans.append(mex)
    childs[p[ds[idx]]].append(base + c[ds[idx]])

print("\n".join([str(a) for a in reversed(ans)]))
