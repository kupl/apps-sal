

MOD = 10**9 + 7


def modFact(x):
    if x < 1:
        raise ValueError
    res = 1
    for i in range(x):
        res = res * (i + 1) % MOD
    return res


def solve(n, m):
    if abs(n - m) > 1:
        return 0
    elif abs(n - m) == 1:
        return modFact(n) * modFact(m) % MOD
    else:
        return modFact(n) * modFact(m) * 2 % MOD


def main():
    N, M = list(map(int, input().split()))
    print((solve(N, M)))
    return


def __starting_point():
    main()


__starting_point()
