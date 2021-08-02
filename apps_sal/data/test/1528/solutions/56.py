n, x = list(map(int, input().split()))
a = [1]
p = [1]

for i in range(n):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    median = (a[n] + 1) // 2

    if x < median:
        return f(n - 1, x - 1)
    elif x == median:
        return p[n - 1] + 1
    else:
        return p[n - 1] + 1 + f(n - 1, x - median)


print((f(n, x)))
