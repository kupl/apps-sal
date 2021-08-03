def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n, m = mi()
g = [input().strip() for i in range(n)]
h = list(zip(*g))

rs = [r for r in range(n) if 'B' in g[r]]
cs = [c for c in range(m) if 'B' in h[c]]
x = (rs[0] + rs[-1]) // 2
y = (cs[0] + cs[-1]) // 2
print(x + 1, y + 1)
