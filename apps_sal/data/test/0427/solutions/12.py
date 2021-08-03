a, b, x, y = map(int, input().split())
l = 0
r = 10000000000000
res = 0


def judge(n, a, b, x, y):
    return (n - n // (x * y)) >= a + b and (n - n // x >= a) and (n - n // y >= b)


while l <= r:
    m = (l + r) // 2
    if judge(m, a, b, x, y):
        r = m - 1
        res = m
    else:
        l = m + 1
print(res)
