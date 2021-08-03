a, b = list(map(int, input().split()))


def f(n):
    if n % 2 == 0:
        n1s = n // 2
        return n if n1s % 2 == 0 else 1 ^ n
    else:
        n1s = (n + 1) // 2
        return 0 if n1s % 2 == 0 else 1


print(f(b) ^ f(a - 1))
