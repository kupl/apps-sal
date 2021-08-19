n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    (x, y, z) = list(map(int, input().split()))
    g[x] += ((y, z),)
    g[y] += ((x, z),)


def go(x, f):
    ret = 0
    for (y, z) in g[x]:
        if y != f:
            ret = max(ret, z + go(y, x))
    return ret


print(go(0, -1))
