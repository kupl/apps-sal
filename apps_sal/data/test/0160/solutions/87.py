import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def resolve():
    (n, k) = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())))
    div = make_divisors(sum(A))
    res = 1
    for x in div:
        B = sorted([a % x for a in A])
        (M, P) = ([0], [0])
        for i in range(n):
            M.append(M[-1] + B[i])
            P.append(P[-1] + x - B[i])
        M.pop(0)
        P.pop(0)
        for i in range(n - 1):
            m = M[i]
            p = P[n - 1] - P[i]
            if m <= k and p <= k and (m % x == p % x):
                res = max(res, x)
    print(res)


def __starting_point():
    resolve()


__starting_point()
