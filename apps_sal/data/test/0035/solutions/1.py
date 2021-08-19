#! /usr/bin/env python3

n, m = list(map(int, input().split()))
a = [input() for i in range(n)]
b = [''.join(a[i][j] for i in range(n)) for j in range(m)]


def check(a, n, m):
    if n % 3 != 0:
        return False
    s = a[0 * n // 3], a[1 * n // 3], a[2 * n // 3]
    if set(s) != set([x * m for x in 'RGB']):
        return False
    for i in range(n):
        if a[i] != s[i * 3 // n]:
            return False
    return True


if check(a, n, m) or check(b, m, n):
    print('YES')
else:
    print('NO')
