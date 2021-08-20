import sys
from collections import Counter
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def prime_factorize(n):
    a = Counter()
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1
    return a


def main():
    N = int(readline())
    prime = Counter()
    for n in range(1, N + 1):
        prime.update(prime_factorize(n))
    C = [0] * 101
    for v in list(prime.values()):
        C[v] += 1
    for i in range(99, -1, -1):
        C[i] += C[i + 1]
    ans = 0
    ans += (C[2] - 2) * (C[4] * (C[4] - 1) // 2)
    ans += (C[2] - 1) * C[24]
    ans += (C[4] - 1) * C[14]
    ans += C[74]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
