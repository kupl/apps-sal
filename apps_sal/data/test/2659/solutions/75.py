import sys


def S(n):
    return n / sum(map(int, str(n)))


def f(n):
    d = 0
    C = [n]
    while S(n) > 10 ** d / 9 * (d + 1):
        c = 10 ** (d + 1) * (n // 10 ** (d + 1) + 1) - 1
        C.append(c)
        d += 1
    Smin = float('inf')
    res = 0
    for c in C:
        if S(c) < Smin:
            Smin = S(c)
            res = c
    return res


def main():
    input = sys.stdin.readline
    K = int(input())
    ans = 1
    for _ in range(K):
        print(ans)
        ans = f(ans + 1)


def __starting_point():
    main()


__starting_point()
