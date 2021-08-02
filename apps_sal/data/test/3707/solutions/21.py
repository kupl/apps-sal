import sys


def solve():
    n, t, k, d = map(int, input().split())

    use = (n + k - 1) // k

    if d < (use - 1) * t:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)


def __starting_point():
    solve()


__starting_point()
