import sys


def check(a, b, c, n, k):
    need = n // 3
    return ((n - k) == (need - a) + (need - b) + (need - c) and a <= need and b <= need and c <= need and a >= 0 and b >= 0 and c >= 0)


for tc in range(int(sys.stdin.readline())):
    n, k, d1, d2 = map(int, sys.stdin.readline().split())
    if n % 3 != 0:
        print('no')
        continue

    ans = False
    # case++
    a = k - 2 * d1 - d2
    if a % 3 == 0:
        a //= 3
        ans |= check(a, a + d1, a + d1 + d2, n, k)

    # case+-
    a = k + d2 - 2 * d1
    if a % 3 == 0:
        a //= 3
        ans |= check(a, a + d1, a + d1 - d2, n, k)

    # case--
    a = k + 2 * d1 + d2
    if a % 3 == 0:
        a //= 3
        ans |= check(a, a - d1, a - d1 - d2, n, k)

    # case-+
    a = k - d2 + 2 * d1
    if a % 3 == 0:
        a //= 3
        ans |= check(a, a - d1, a - d1 + d2, n, k)

    print('yes' if ans else 'no')
