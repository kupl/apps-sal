import collections
import math

n = int(input())
p = list(map(int, input().split()))
s = input()


def solve(p, s):
    a, b = [0] * n, [0] * n
    m = 0
    if s[0] == 'B':
        b[0] = p[0]
        m += p[0]
    else:
        a[0] = p[0]
    for i in range(1, n):
        if s[i] == 'B':
            b[i] += p[i]
            m += p[i]
        else:
            a[i] += p[i]
        a[i] += a[i - 1]
        b[i] += b[i - 1]
    ans = m
    for i in range(n):
        if m - b[i] + a[i] > ans:
            ans = m - b[i] + a[i]
    return ans


print(max(solve(p, s), solve(p[::-1], s[::-1])))
