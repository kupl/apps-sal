MOD = 998244353


def solve(A, B, C):
    tmp = 1
    tmp *= A * (A + 1) // 2
    tmp %= MOD
    tmp *= B * (B + 1) // 2
    tmp %= MOD
    tmp *= C * (C + 1) // 2
    tmp %= MOD
    return tmp


def main():
    (A, B, C) = list(map(int, input().split()))
    a = solve(A, B, C)
    print(a)


def __starting_point():
    main()


__starting_point()
