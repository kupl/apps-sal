# coding=utf-8
import sys


R = lambda: list(map(int, input().split()))


def f(l, r):
    ans = sum(a[l:r + 1])

    a1 = sorted(a[l:r + 1])
    a2 = sorted(a[:l] + a[r + 1:], reverse=True)


    for i in range(min(k, len(a1), len(a2))):
        m = min(a1)
        if a2[i] > m:
            ans += a2[i] - m
            a1[a1.index(m)] = a2[i]

    return ans


n, k = R()

a = R()

print(max(f(l,r) for l in range(n) for r in range(l,n)))
