import sys
input = sys.stdin.readline


def f(x):
    ans = 0
    for i in range(n):
        if a[i] <= x:
            continue
        ans += b[i]
    if ans <= x:
        return 1
    return 0


def bsearch(l, r):
    m = (l + r) // 2
    if f(m):
        if f(m - 1) == 0:
            return m
        return bsearch(l, m - 1)
    return bsearch(m + 1, r)


t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    a = [int(i) for i in l]
    l = input().split()
    b = [int(i) for i in l]
    print(bsearch(0, 10 ** 9 + 5))
