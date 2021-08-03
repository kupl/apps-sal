from functools import reduce
# https://drken1215.hatenablog.com/entry/2020/01/26/164200
# bit_pathの参考にした


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
            if ~res:  # -1以外
                return res | (1 << e.edge_id)
        return -1

    N = int(input())

    g = tuple(set() for _ in range(N))
    for edge_id in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add(Edge(to=b, edge_id=edge_id))
        g[b].add(Edge(to=a, edge_id=edge_id))

    M = int(input())

    cons = []
    for _ in range(M):
        u, v = (int(x) - 1 for x in input().split())
        b = bit_path(u, v)
        cons.append(b)

    ans = 1 << (N - 1)
    for k in range(1, M + 1):
        for comb in combinations(cons, r=k):
            b = reduce(or_, comb)
            ans += ((-1) ** k) * (1 << (N - 1 - bin(b).count('1')))
    print(ans)


def __starting_point():
    main()


__starting_point()
