def solve():
    n = int(input())
    k = int(input())
    ans = 1
    for i in range(n):
        if ans < k:
            ans *= 2
        else:
            ans += k
    print(ans)


def __starting_point():
    solve()


__starting_point()
