def calc(n, m):
    r = 1
    for i in range(n, n + 2 * m):
        r *= i
    for i in range(1, 2 * m + 1):
        r //= i
    return r % (10**9 + 7)


T = 1
for _ in range(T):
    a, b = [int(x) for x in input().split()]
    print(calc(a, b))
