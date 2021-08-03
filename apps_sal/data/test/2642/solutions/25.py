import sys
import os

if 'local' in os.environ:
    sys.stdin = open('./input.txt', 'r')


def f(): return list(map(int, input().split()))


def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


def quick_pow(x, n, mod):
    ans = 1
    while n:
        if n & 1:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n >>= 1

    return ans


def solve():
    mod = 1000000007
    n = f()[0]

    dirs = {}

    all0 = 0
    x0 = 0
    y0 = 0

    for _ in range(n):
        a, b = f()
        if a == 0 and b == 0:
            all0 += 1
            continue
        if a == 0:
            x0 += 1
            continue
        if b == 0:
            y0 += 1
            continue

        if a < 0:
            a = -a
            b = -b
        g = gcd(abs(a), abs(b))
        a //= g
        b //= g

        if a * b > 0:
            if (a, b) not in dirs:
                dirs[(a, b)] = {}
                dirs[(a, b)][0] = 0
                dirs[(a, b)][1] = 0
            dirs[(a, b)][0] = dirs[(a, b)][0] + 1
        else:
            if (-b, a) not in dirs:
                dirs[(-b, a)] = {}
                dirs[(-b, a)][0] = 0
                dirs[(-b, a)][1] = 0
            dirs[(-b, a)][1] = dirs[(-b, a)][1] + 1

    ans = 1
    ans *= (quick_pow(2, x0, mod) + quick_pow(2, y0, mod) - 1 + mod) % mod

    ans %= mod
    for _, l in list(dirs.items()):
        ans *= (quick_pow(2, l[0], mod) + quick_pow(2, l[1], mod) - 1 + mod) % mod
        ans %= mod

    ans -= 1
    if all0:
        ans += all0

    ans += mod
    ans %= mod
    print(ans)


solve()
