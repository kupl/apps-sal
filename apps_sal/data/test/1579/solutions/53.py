import sys
sys.setrecursionlimit(10**6)


def dfs(x, al):
    nonlocal cntx, cnty
    if (al, x) in used:
        return
    used.add((al, x))
    if al == 0:
        cntx += 1
    else:
        cnty += 1
    for xy in to[al][x]:
        dfs(xy, 1 - al)
    return


n = int(input())
to = [{}, {}]
for _ in range(n):
    x, y = list(map(int, input().split()))
    to[0].setdefault(x, [])
    to[1].setdefault(y, [])
    to[0][x] += [y]
    to[1][y] += [x]
used = set()
ans = 0
for x in list(to[0].keys()):
    if (0, x) in used:
        continue
    cntx = 0
    cnty = 0
    dfs(x, 0)
    ans += cntx * cnty
print((ans - n))
