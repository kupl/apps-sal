import sys
sys.setrecursionlimit(10000000)
(n, k) = list(map(int, input().split()))
CONST = 10 ** 9 + 7
path = {i: list() for i in range(n)}
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
used = [0] * n
used[0] = 1


def bfs(pos, parent):
    res = k - parent
    if parent > 0:
        deg = 2
    else:
        deg = 1
    for nex in path[pos]:
        if used[nex]:
            continue
        used[nex] = 1
        res *= bfs(nex, deg)
        res = res % CONST
        deg += 1
    return res % CONST


print(bfs(0, 0))
