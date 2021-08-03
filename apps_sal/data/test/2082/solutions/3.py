def main():
    n, m = list(map(int, input().split()))
    l = [int(i) for i in input().split()]
    rank, ans = [], 0
    for i in range(m):
        a, b = list(map(int, input().split()))
        a, b = a - 1, b - 1
        rank.append((min(l[a], l[b]), a, b))

    rank = sorted(rank, key=lambda x: -x[0])
    par = list(range(n))
    siz = [1] * n
    ans = 0.0

    def find(a):
        root = a
        while root != par[root]:
            root = par[root]
        while a != par[a]:
            newp = par[a]
            par[a] = root
            a = newp
        return root

    def merge(a, b, i):
        a = find(a)
        b = find(b)
        if a == b:
            return 0
        add = siz[a] * siz[b]
        siz[a] += siz[b]
        par[b] = a
        return (add * i[0]) / (n * (n - 1))

    for i in rank:
        ans += merge(i[1], i[2], i)

    print("%.12f" % (2 * ans))


def __starting_point():
    main()


__starting_point()
