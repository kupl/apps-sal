def LI():
    return list(map(int, input().split()))


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


N, M, K = LI()
par = [-1]*N
not_kouho = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    unite(a - 1, b - 1)
    not_kouho[a-1].append(b-1)
    not_kouho[b-1].append(a-1)

for i in range(K):
    a, b = map(int, input().split())
    if same(a-1, b-1):
        not_kouho[a-1].append(b-1)
        not_kouho[b-1].append(a-1)

for i in range(N):
    print(size(i)-len(not_kouho[i])-1, end=" ")

