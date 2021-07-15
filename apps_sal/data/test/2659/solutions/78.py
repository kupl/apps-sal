from math import log10, ceil


def S(n: int) -> int:
    """n を十進法で表した時の各桁のあたいの総和
    :param n: 任意の正の整数
    :return: 十進法の各桁の和
    """
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def f(N: int) -> int:
    if N < 10:
        return N

    D = ceil(log10(N) + 1)
    x = 10 * (N // 10 + 1) - 1
    for d in range(1, D + 1):
        td = 10 ** (d + 1)
        nx = td * (N // td + 1) - 1

        if nx / S(nx) < x / S(x):
            x = nx
    return x


def __starting_point():
    K = int(input())
    N = 1
    for _ in range(K):
        print(N)
        N = f(N+1)

__starting_point()
