# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

N, M = list(map(int, input().split()))
AB_M = [list(map(int, input().split())) for _ in range(M)]

# union find
parents = [-1] * (N + 1)


def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x


for ab in AB_M:
    union(ab[0], ab[1])

ans = - min(parents)

print(ans)
