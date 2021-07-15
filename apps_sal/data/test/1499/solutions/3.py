def solve():
    N, M = list(map(int, input().split()))

    ans = []

    def app(x):
        if x < M:
            ans.append(str(x + 1))

    for i in range(0, N * 2, 2):
        app(N * 2 + i)
        app(i)
        app(N * 2 + i + 1)
        app(i + 1)

    print(' '.join(ans))


def __starting_point():
    solve()

__starting_point()
