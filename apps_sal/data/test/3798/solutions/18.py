# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, s = list(map(int, read().split()))


def f(b, n):
    r = 0
    while n:
        r += n % b
        n //= b
    return r


M = 4 * 10**5

ans = -1
for i in range(2, M):
    if f(i, n) == s:
        print(i)
        break
else:
    for x in range(M, 0, -1):
        if (n - s) % x == 0:
            b = (n - s) // x + 1
            # print(b)
            if x < b and 0 <= s - x < b:
                print(b)
                break
    else:
        if n == s:
            print((n + 1))
        else:
            print((-1))
