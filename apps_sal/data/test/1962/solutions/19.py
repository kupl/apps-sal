def R(): return list(map(int, input().split()))


n, k, l = R()
a = list(R())
a.sort()


def func():
    if n == 1:
        return a[0]

    r = (n - 1) * k
    while a[r] - a[0] > l:
        r -= 1
    if r < n - 1:
        return 0

    res = a[0] + a[r]

    for i in range(n - 2, 0, -1):
        if i * k >= r - 1:
            res += a[r - 1]
            r -= 1
        else:
            res += a[i * k]

    return res


print(func())
