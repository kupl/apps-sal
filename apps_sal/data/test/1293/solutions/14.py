def solve():
    N = int(input())
    B = list(map(int, input().split()))
    h = 0
    ans = 0
    for b in B:
        ans += abs(h - b)
        h = b
    print(ans)


def __starting_point():
    solve()


__starting_point()
