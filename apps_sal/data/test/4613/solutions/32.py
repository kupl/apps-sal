import itertools
N, M = list(map(int, input().split()))
ABs = [list(map(int, input().split())) for _ in range(M)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y
    size[y] = size[x] + size[y]
    size[x] = 0


loop_list = list(itertools.combinations(ABs, M - 1))

ans = 0
for loop in loop_list:
    par = [i for i in range(N + 1)]
    size = [1 for _ in range(N + 1)]

    for bridge in loop:
        unite(bridge[0], bridge[1])

    if(max(size) != N):
        ans += 1

print(ans)
