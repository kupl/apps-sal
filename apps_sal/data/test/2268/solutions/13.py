def solve():
    N, M = list(map(int, input().split()))
    name = input()

    td = {}
    for c in 'abcdefghijklmnopqrstuvwxyz':
        td[c] = c

    for i in range(M):
        p, m = input().split()
        if p == m:
            continue
        pt = td[p]
        mt = td[m]
        del td[p]
        del td[m]
        td[m] = pt
        td[p] = mt

    nd = {f: t for t, f in list(td.items())}

    ans = ''.join([nd[c] for c in name])

    print(ans)


def __starting_point():
    solve()

__starting_point()
