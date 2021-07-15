def solve():
    X, Y = [int(i) for i in input().split()]
    ans = 0
    while X <= Y:
        ans += 1
        X *= 2
    print(ans)


def __starting_point():
    solve()
__starting_point()
