# create date: 2020-07-05 10:13

import sys
stdin = sys.stdin

mod = 10**9 + 7


def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    a = na()
    ans = 0
    for i in range(61):
        cnt = 0
        for ai in a:
            if (ai >> i) & 1:
                cnt += 1
        ans += ((cnt * (n - cnt)) * 2**i) % mod
    ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
