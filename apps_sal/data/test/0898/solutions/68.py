def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


def solve(N, M):
    div = divisor(M)
    div.sort()
    ans = 0
    for d in div:
        if M // d >= N:
            ans = d
    print(ans)


def __starting_point():
    (N, M) = list(map(int, input().split()))
    solve(N, M)


__starting_point()
