def solve(N, As):
    S = sum(As)
    Xs = [0] * N
    Xs[0] = S - (sum(As[1::2]) * 2)
    for i in range(1, N):
        Xs[i] = 2 * As[i - 1] - Xs[i - 1]
    print((' '.join([str(i) for i in Xs])))


def __starting_point():
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)


__starting_point()
