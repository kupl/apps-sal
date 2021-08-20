from functools import reduce


def main():
    from collections import namedtuple
    from functools import reduce
    from itertools import combinations
    from operator import or_
    Edge = namedtuple('Edge', 'to edge_id')

    def bit_path(curr, goal, par=-1):
        if curr == goal:
            return 0
        for e in g[curr]:
            if e.to == par:
                continue
            res = bit_path(curr=e.to, goal=goal, par=curr)
            if ~res:
                return res | 1 << e.edge_id
        return -1

    def popcnt(n):
        """https://atcoder.jp/contests/abc152/submissions/9619555"""
        c = (n & 6148914691236517205) + (n >> 1 & 6148914691236517205)
        c = (c & 3689348814741910323) + (c >> 2 & 3689348814741910323)
        c = (c & 1085102592571150095) + (c >> 4 & 1085102592571150095)
        c = (c & 71777214294589695) + (c >> 8 & 71777214294589695)
        c = (c & 281470681808895) + (c >> 16 & 281470681808895)
        c = (c & 4294967295) + (c >> 32 & 4294967295)
        return c
    N = int(input())
    g = tuple((set() for _ in range(N)))
    for edge_id in range(N - 1):
        (a, b) = (int(x) - 1 for x in input().split())
        g[a].add(Edge(to=b, edge_id=edge_id))
        g[b].add(Edge(to=a, edge_id=edge_id))
    M = int(input())
    cons = []
    for _ in range(M):
        (u, v) = (int(x) - 1 for x in input().split())
        b = bit_path(u, v)
        cons.append(b)
    ans = 1 << N - 1
    for k in range(1, M + 1):
        for comb in combinations(cons, r=k):
            b = reduce(or_, comb)
            ans += (-1) ** k * (1 << N - 1 - popcnt(b))
    print(ans)


def __starting_point():
    main()


__starting_point()
