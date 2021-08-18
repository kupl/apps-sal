
def resolve():
    N, M = map(int, input().split())

    ans = 1
    for A in range(1, int(M ** 0.5) + 1):
        if M % A != 0:
            continue
        B = M // A
        if N * A <= M:
            ans = max(ans, A)
        if N * B <= M:
            ans = max(ans, B)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
