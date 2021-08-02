def solve():
    N, A, B = list(map(int, input().split()))

    A -= 1
    A += N * 100

    A += B

    A %= N

    A += 1

    print(A)


def __starting_point():
    solve()


__starting_point()
