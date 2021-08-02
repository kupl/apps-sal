n, x = list(map(int, input().split()))
p = [1] * -~n
l = [1] * -~n
for i in range(1, n + 1):
    p[i] = p[i - 1] * 2 + 1
    l[i] = l[i - 1] * 2 + 3


def rec(m, y):
    if y == 0:
        return 0
    if m == 0:
        return 1
    h = l[m] // 2
    if h < y:
        return 1 + p[m - 1] + rec(m - 1, y - h - 1)
    else:
        return rec(m - 1, y - 1)


print((rec(n, x)))
