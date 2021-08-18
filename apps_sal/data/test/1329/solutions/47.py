import sys
import math
import collections
import bisect
import copy


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    n = ni()
    divisor = [0 for _ in range(101)]

    ans = 0
    for i in range(1, n + 1):
        a = prime_factorize(i)
        for ai in a:
            divisor[ai] += 1

    over75 = 0
    over25 = 0
    over15 = 0
    over5 = 0
    over3 = 0
    for di in divisor:
        tmp = di + 1
        if tmp >= 75:
            over75 += 1
        if tmp >= 25:
            over25 += 1
        if tmp >= 15:
            over15 += 1
        if tmp >= 5:
            over5 += 1
        if tmp >= 3:
            over3 += 1

    ans = over75 + over25 * (over3 - 1) + over15 * (over5 - 1) + over5 * (over5 - 1) // 2 * (over3 - 2)

    print(ans)


def __starting_point():
    main()


__starting_point()
