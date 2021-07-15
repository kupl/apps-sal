def solve(X, Y, A, B):
    d, r = divmod(Y - X, A + B)
    if r == 0:
        return d
    else:
        return -1


def __starting_point():
    T, = list(map(int, input().split()))
    for t in range(T):
        X, Y, A, B = list(map(int, input().split()))
        ans = solve(X, Y, A, B)
        print(ans)

__starting_point()
