def gen(n):
    x = n
    d = 2
    cnt = 0
    while x % d == 0:
        x //= d
        cnt += 1
    yield cnt
    d = 3
    while d * d <= n:
        cnt = 0
        while x % d == 0:
            x //= d
            cnt += 1
        yield cnt
        d += 2
    if x > 1:
        yield 1


def main():
    MOD = 10 ** 9 + 7
    (N, M) = list(map(int, input().split()))
    ans = 1
    for cnt in gen(M):
        for d in range(cnt):
            ans = ans * (N - 1 + cnt - d) % MOD * pow(d + 1, MOD - 2, MOD) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
