
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


N, M = map(int, input().split())
bridges = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    bridges.append((a, b))

par = [-1] * N
tot = N * (N - 1) // 2
ans = [tot]

for a, b in bridges[::-1]:
    if not same(a, b):
        tot -= size(a) * size(b)
    unite(a, b)
    ans.append(tot)

print('\n'.join(map(str, ans[:-1][::-1])))
