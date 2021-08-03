import sys
import collections

stdin = sys.stdin
n, m = map(int, stdin.readline().split())

par = [i for i in range(n)]
size = [1] * n  # size of tree
rank = [1] * n  # distance from parent


def find(x, par):
    if par[x] == x:
        return x
    else:
        return find(par[x], par)


def unite(x, y):
    x = find(x, par)
    y = find(y, par)

    if x != y:
        # xとyの属している集合が異なる時
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1


for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    unite(x - 1, y - 1)

ans = set()
for i in range(n):
    ans.add(find(i, par))
print(len(ans))
