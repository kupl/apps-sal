def readinput():
    (n, m) = list(map(int, input().split()))
    x = list(map(int, input().split()))
    return (n, m, x)


def main(n, m, x):
    if m <= n:
        return 0
    xs = sorted(x)
    d = []
    for i in range(m - 1):
        d.append((xs[i + 1] - xs[i], i + 1))
    ds = sorted(d, reverse=True, key=lambda x: x[0])
    c = [0] * m
    for i in range(n - 1):
        c[ds[i][1]] += 1
    ans = 0
    for i in range(1, m):
        if c[i] == 0:
            ans += xs[i] - xs[i - 1]
    return ans


def __starting_point():
    (n, m, x) = readinput()
    ans = main(n, m, x)
    print(ans)


__starting_point()
