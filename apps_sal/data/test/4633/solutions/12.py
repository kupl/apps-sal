import sys
from math import ceil
input = sys.stdin.readline
t = int(input())


def f(n):
    r = 0
    while n:
        r += n % 10
        n //= 10
    return r


for tc in range(t):
    (n, s) = list(map(int, input().strip().split()))
    if f(n) <= s:
        print(0)
        continue
    b = 1
    ans = int(1e+20)
    while b <= n * 10:
        rn = n // b * b + b
        if f(rn) <= s:
            ans = min(ans, rn - n)
        b *= 10
    print(ans)
