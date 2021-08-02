MODULO = 1000000007


def fast_pow(x):
    if x == 1:
        return 2
    if x == 0:
        return 1
    prev = fast_pow(x // 2)
    add = 1 if x % 2 == 0 else 2
    return (prev * prev * add) % MODULO


n, m, k = map(int, input().split())

if k == -1 and n % 2 != m % 2:
    print(0)
else:
    print(fast_pow(n * m - n - m + 1))
