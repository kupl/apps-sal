def solve(X, Y):
    ans = 0
    tmp = X
    while tmp <= Y:
        ans += 1
        tmp *= 2

    return ans


def __starting_point():
    X, Y = list(map(int, input().split()))
    print((solve(X, Y)))

__starting_point()
