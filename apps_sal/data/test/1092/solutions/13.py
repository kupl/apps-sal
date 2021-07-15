# https://codeforces.com/problemset/problem/294/C

import sys
import math

mod = 10 ** 9 + 7


def factorial(n):
    x = 1
    for i in range(n):
        yield x
        x = x * (i + 1) % mod


f = list(factorial(1001))


def C(n, k):
    return f[n] * pow(f[k], mod - 2, mod) * pow(f[n - k], mod - 2, mod) % mod


def main():
    # sys.stdin = open('E:\\Sublime\\in.txt', 'r')
    # sys.stdout = open('E:\\Sublime\\out.txt', 'w')
    # sys.stderr = open('E:\\Sublime\\err.txt', 'w')

    # n = int(sys.stdin.readline().strip())
    # a, b = map(int, sys.stdin.readline().strip().split()[:2])

    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    b = [-1] + [int(x) - 1 for x in sys.stdin.readline().strip().split()] + [n]
    b.sort()

    ans = 1
    cur = n - m
    for i in range(1, len(b)):
        l = b[i] - b[i - 1] - 1
        ans = ans * C(cur, l) % mod
        if (l > 0) and (i > 1) and (i < len(b) - 1):
            ans = ans * pow(2, l - 1, mod) % mod
        cur -= l

    print(ans)


def __starting_point():
    main()

# hajj
#  　　　　　　 ＿＿
# 　　　　　／＞　　フ
# 　　　　　| 　_　 _ l
# 　 　　　／` ミ＿xノ
# 　　 　 /　　　 　 |
# 　　　 /　 ヽ　　 ﾉ
# 　 　 │　　|　|　|
# 　／￣|　　 |　|　|
# 　| (￣ヽ＿_ヽ_)__)
# 　＼二つ

__starting_point()
