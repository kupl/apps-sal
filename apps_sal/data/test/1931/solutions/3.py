import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('B.txt').readlines())

    def input():
        return next(f)
else:
    input = sys.stdin.readline


def func(k):
    return (k * (k + 1)) // 2 * 3 - k


t = int(input())
for _ in range(t):
    n = int(input())

    res = 0
    k = 1
    while func(k) <= n:
        k += 1
    while n > 0:
        while k > 0 and func(k) > n:
            k -= 1
        if k != 0:
            res += 1
            n -= func(k)
        else:
            break
    print(res)
