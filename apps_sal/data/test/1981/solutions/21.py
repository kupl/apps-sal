def fill(e, f, g):
    n = [g]
    while n:
        d = n.pop()
        for p in e[d]:
            if len(f[p]) == 0:
                f[d].add(p)
                n.append(p)


def count_cats(f, a, m, n, c):
    s = 0
    nodes = [(n, c)]
    while nodes:
        n, c = nodes.pop()
        z = a[n]
        t = z + c if z else 0
        if t <= m:
            if len(f[n]) == 0:
                s += 1
            else:
                for j in f[n]:
                    nodes.append((j, t))
    return s


def solve(n, m, a, e):
    f = []
    for i in range(n):
        f.append(set())
    fill(e, f, 0)
    s = count_cats(f, a, m, 0, 0)
    return s


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    e = []
    for i in range(n):
        e.append(set())
    for i in range(n - 1):
        p = tuple(map(int, input().split()))
        e[p[0] - 1].add(p[1] - 1)
        e[p[1] - 1].add(p[0] - 1)
    print(solve(n, m, a, e))


def __starting_point():
    main()


__starting_point()
