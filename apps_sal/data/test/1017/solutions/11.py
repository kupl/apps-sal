def solve():
    N = int(input())

    d3 = N // 3

    m3 = N % 3

    ans = d3 * 2

    if m3 == 1:
        ans += 1
    elif m3 == 2:
        ans += 1

    print(ans)


def __starting_point():
    solve()


__starting_point()
