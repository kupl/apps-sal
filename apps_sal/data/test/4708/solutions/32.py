def solve():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    print((x * min(n, k) + y * max(n-k,0)))


def __starting_point():
    solve()

__starting_point()
