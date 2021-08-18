n = int(input())
m = (1 << (n + 1)) - 1
a = [0] + list(map(int, input().split()))

max_value = 0


def precalc(i, prev):
    nonlocal max_value
    if i < m:
        a[i] += prev
        if a[i] > max_value:
            max_value = a[i]
        precalc((i << 1) + 1, a[i])
        precalc((i << 1) + 2, a[i])


def calc(i):
    if i >= (1 << n) - 1:
        return 0
    x = (i << 1) + 1
    y = (i << 1) + 2
    result = calc(x) + calc(y)
    a[i] = max(a[x], a[y])
    return result + a[i] - min(a[x], a[y])


precalc(0, 0)
print(calc(0))
