import sys
import numpy as np
input = sys.stdin.readline


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors


def main():
    n, k = map(int, input().split())
    a = np.array([int(x) for x in input().split()])
    key = make_divisors(np.sum(a))

    for v in key:
        mod = np.sort(a % v)
        c1, c2 = 0, np.sum(mod)
        judge = c2
        for i in range(n - 1, -1, -1):
            c1 += v - mod[i]
            c2 -= mod[i]
            judge = min(judge, max(c1, c2))
        if judge <= k:
            print(v)
            return


def __starting_point():
    main()


__starting_point()
