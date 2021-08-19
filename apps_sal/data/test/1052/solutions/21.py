(n, k) = list(map(int, input().split()))


def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n - 1) * (f(n - 1) + f(n - 2))


def g(n, k):
    res = 1
    for i in range(1, k + 1):
        res *= n - i + 1
        res //= i
    return res


res = 1
for i in range(1, k + 1):
    res += g(n, i) * f(i)
print(res)
