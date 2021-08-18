def binPow(x, n, r):
    if n == 0:
        return 1
    elif n == 1:
        return x % r
    if n % 2 == 0:
        return binPow((x * x) % r, n // 2, r)
    return (binPow((x * x) % r, n // 2, r) * x) % r


x, k = list(map(int, input().split()))
r = 10 ** 9 + 7
if x == 0:
    print(0)
    return
elif k == 0:
    print((x * 2) % r)
    return
print((binPow(2, k, r) * (2 * x - 1) + 1) % r)
