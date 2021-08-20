def LI():
    return list(map(int, input().split()))


N = int(input())
C = LI()
MOD = 10 ** 9 + 7


def main():
    ans = 0
    C.sort()
    for i in range(N):
        x = C[i] * (N - i + 1) % MOD
        ans = (ans + x) % MOD
    ans = ans * pow(4, N - 1, MOD) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
