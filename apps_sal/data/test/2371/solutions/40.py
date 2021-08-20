def solve():
    (N, Z, W) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if N == 1:
        print(abs(a[0] - W))
        return
    print(max(abs(a[-1] - W), abs(a[-2] - a[-1])))


def __starting_point():
    solve()


__starting_point()
