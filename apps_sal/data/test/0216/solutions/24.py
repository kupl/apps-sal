def solve():
    n = int(input())
    A = list(map(int, input().split()))
    res = 0
    for a in A:
        if a >= 0:
            res += a
        else:
            res -= a
    print(res)


def __starting_point():
    solve()


__starting_point()
