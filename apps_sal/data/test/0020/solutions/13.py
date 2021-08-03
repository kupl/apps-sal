import sys


def solve():
    s = input()

    m = timetomin(s)
    ans = 0

    while (not is_pali(mintotime(m))):
        m += 1
        m %= 24 * 60
        ans += 1

    print(ans)


def is_pali(s):
    return s == s[::-1]


def mintotime(m):
    return '{:02d}:{:02d}'.format(m // 60, m % 60)


def timetomin(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m


def __starting_point():
    solve()


__starting_point()
