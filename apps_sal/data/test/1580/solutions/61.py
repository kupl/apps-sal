from networkx.utils import UnionFind


def main():
    (n, m) = map(int, input().split())
    uf = UnionFind()
    for i in range(n):
        _ = uf[i]
    for _ in range(m):
        (x, y, z) = map(int, input().split())
        uf.union(x - 1, y - 1)
    print(len(list(uf.to_sets())))


def __starting_point():
    main()


__starting_point()
