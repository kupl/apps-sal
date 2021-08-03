def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
g = [[] for i in range(n + 1)]
for i in range(2, n + 1):
    x = ii()
    g[x].append(i)
l = set(i for i in range(1, n + 1) if not g[i])
c = sum(sum(j in l for j in g[i]) >= 3 for i in range(1, n + 1))
print('Yes' if c + len(l) == n else 'No')
