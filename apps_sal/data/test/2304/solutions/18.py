def main():
    import sys
    input = sys.stdin.readline

    def find(x):
        if par[x] < 0:
            return x
        else:
            px = find(par[x])
            wei[x] += wei[par[x]]
            par[x] = px
            return px

    def weight(x):
        find(x)
        return wei[x]

    def unite(x, y, w):
        w += wei[x] - wei[y]
        x = find(x)
        y = find(y)

        if x == y:
            return False
        else:
            if par[x] > par[y]:
                x, y = y, x
                w = -w
            par[x] += par[y]
            par[y] = x
            wei[y] = w
            return True

    def same(x, y):
        return find(x) == find(y)

    def size(x):
        return -par[find(x)]

    def diff(x, y):
        return weight(y) - weight(x)

    n, m = map(int, input().split())

    par = [-1] * n
    wei = [0] * n

    for i in range(m):
        l, r, d = map(int, input().split())
        l, r = l - 1, r - 1
        if same(l, r):
            if d != diff(l, r):
                print('No')
                return
        else:
            unite(l, r, d)
    print('Yes')


def __starting_point():
    main()


__starting_point()
