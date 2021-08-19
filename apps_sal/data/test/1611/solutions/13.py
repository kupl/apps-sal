def solve():
    N = int(input())
    L = list(map(int, input().split()))
    ma = max(L)
    re = sum(L) - ma
    ans = ma - re + 1
    print(ans)


def __starting_point():
    solve()


__starting_point()
