def func(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    k = int(n / 2)
    remain = n - k * 2
    return k + func(k + remain)


inf = list(map(int, input().split()))
n, b, p = inf[0], inf[1], inf[2]
water = 2 * b + 1
match = func(n)
print(match * water, n * p)
