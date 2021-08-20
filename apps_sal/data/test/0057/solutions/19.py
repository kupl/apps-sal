def solve():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        (X[i], Y[i]) = list(map(int, input().split()))
    xs = list(set(X))
    ys = list(set(Y))
    if len(xs) == 1 or len(ys) == 1:
        print(-1)
        return
    print(abs(xs[1] - xs[0]) * abs(ys[1] - ys[0]))


def __starting_point():
    solve()


__starting_point()
