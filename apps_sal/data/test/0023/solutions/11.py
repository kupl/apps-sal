def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n - 1)


def g(ls, i, s):
    if len(ls) == 1:
        return 10 * s + ls[0]
    else:
        k = f(len(ls) - 1)
        return g(ls[:i // k] + ls[i // k + 1:], i % k, 10 * s + ls[i // k])


a = int(input())
b = int(input())
ls = list(sorted(map(int, str(a))))
l = 0
r = f(len(ls)) - 1
if g(ls, r, 0) <= b:
    ans = g(ls, r, 0)
else:
    while 1 < r - l:
        c = (l + r) // 2
        if b < g(ls, c, 0):
            r = c
        else:
            l = c
    ans = g(ls, l, 0)
print(ans)

