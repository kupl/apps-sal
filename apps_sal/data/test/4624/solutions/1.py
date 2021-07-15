import sys, math


input = lambda: sys.stdin.readline().rstrip()


def gcd(n, f):
    if n == 0 or f == 0:
        return max(n, f)
    if n > f:
        return gcd(n % f, f)
    else:
        return gcd(f % n, n)


def division_with_remainder_up(pp, ppp):
    return (pp + ppp - 1) // ppp


for i in range(int(input())):
    n, k = map(int, input().split())
    n -= 2
    if n <= 0:
        print(1)
    else:
        print(division_with_remainder_up(n,k)+1)
