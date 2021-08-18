n, x = map(int, input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(2 * a[-1] + 3)
    p.append(a[-1] // 2 + 1)


def f(n, x):
    if n == 0:
        if x >= 1:
            return 1
        else:
            return 0
    elif x == 1:
        return 0
    elif x == a[n]:
        return p[n]
    elif x == a[n - 1] + 2:
        return p[n - 1] + 1
    elif 1 < x < a[n - 1] + 2:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - a[n - 1] - 2)


print(f(n, x))
