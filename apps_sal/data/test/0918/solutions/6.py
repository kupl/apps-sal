def solve():
    N, M = list(map(int, input().split()))

    ds = [[] for _ in range(M)]
    for i in range(N):
        name, dn, score = input().split()
        dn = int(dn) - 1
        ds[dn].append((-int(score), name))

    for i in range(M):
        ps = ds[i]
        ps.sort()
        if len(ps) == 2:
            print('%s %s' % (ps[0][1], ps[1][1]))
        else:
            if ps[1][0] == ps[2][0]:
                print('?')
            else:
                print('%s %s' % (ps[0][1], ps[1][1]))


def __starting_point():
    solve()


__starting_point()
