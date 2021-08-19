(N, M, K) = map(int, input().split())
par = [0] * (N + 1)
num = [0] * (N + 1)
group = [1] * (N + 1)
for i in range(1, N + 1):
    par[i] = i


def root(x):
    if par[x] == x:
        return x
    return root(par[x])


def union(x, y):
    rx = root(x)
    ry = root(y)
    if rx == ry:
        return
    par[max(rx, ry)] = min(rx, ry)
    group[min(rx, ry)] += group[max(rx, ry)]


def same(x, y):
    return root(x) == root(y)


for _ in range(M):
    (a, b) = map(int, input().split())
    union(a, b)
    num[a] += 1
    num[b] += 1
for _ in range(K):
    (c, d) = map(int, input().split())
    if same(c, d):
        num[c] += 1
        num[d] += 1
for i in range(1, N + 1):
    print(group[root(i)] - num[i] - 1, end=' ')
