import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def gcd(n, f):
    if n == 0 or f == 0:
        return max(n, f)
    if n > f:
        return gcd(n % f, f)
    else:
        return gcd(f % n, n)


def division_with_remainder_up(pp, ppp):
    return (pp + ppp - 1) // ppp


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    mas = []
    ans = 'NO'
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        (v, c) = list(map(int, input().split()))
        if b == v:
            ans = 'YES'
    if m % 2 == 0:
        print(ans)
    else:
        print('NO')
