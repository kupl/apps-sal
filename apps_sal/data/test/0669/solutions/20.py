import bisect
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
x, y = set(), set()


def f(x, n, i, s=0):
    if i == n:
        x.add(s % m)
    else:
        f(x, n, i + 1, s + a[i])
        f(x, n, i + 1, s)


h = n // 2
f(x, h, 0)
f(y, n, h)
y = sorted(y)
k = 0
print(max(i + y[bisect.bisect_left(y, m - i) - 1]for i in x))
