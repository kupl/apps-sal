import sys
n, l, r = map(int, input().split())
l -= 1
r -= 1


def cnt(n):
    if n <= 1:
        return 1
    return 2 * cnt(n // 2) + 1


def rec(n, s, e):
    if s > e:
        return 0
    if s > r or e < l:
        return 0;
    if n <= 1:
        return n
    mid = (s + e) // 2
    plus = 0
    if l <= mid <= r:
        plus = n % 2
    return rec(n // 2, s, mid - 1) + rec(n // 2, mid + 1, e) + plus


length = cnt(n)
print(rec(n, 0, length - 1))
