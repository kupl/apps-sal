def solve():
    (n, m, k) = list(map(int, input().split()))
    h = set(map(int, input().split()))
    pos = 1
    for i in range(k):
        (u, v) = list(map(int, input().split()))
        if pos != u:
            (u, v) = (v, u)
        if pos == u:
            if u not in h:
                pos = v
    print(pos)


def __starting_point():
    solve()


__starting_point()
