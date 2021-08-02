def slove():
    A, B, K = map(int, input().split())
    if A > K:
        print(A - K, B)
    else:
        print(0, max(0, -K + (A + B)))


def __starting_point():
    slove()


__starting_point()
