def iroha():
    A, B, C = map(int, input().split())
    S = A + B + C
    if S == 17:
        print("YES")
    else:
        print("NO")


def __starting_point():
    iroha()


__starting_point()
