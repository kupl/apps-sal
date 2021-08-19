def f(n):
    if n < 10:
        return n
    if n < 100:
        return 9 + 2 * (n - 9)
    if n < 1000.0:
        return f(99) + 3 * (n - 99)
    if n < 10000.0:
        return f(999) + 4 * (n - 999)
    if n < 100000.0:
        return f(9999) + 5 * (n - 9999)
    if n < 1000000.0:
        return f(99999) + 6 * (n - 99999)
    if n < 10000000.0:
        return f(999999) + 7 * (n - 999999)
    if n < 100000000.0:
        return f(9999999) + 8 * (n - 9999999)
    if n < 1000000000.0:
        return f(99999999) + 9 * (n - 99999999)
    return f(999999999) + 10 * (n - 999999999)


n = int(input())
print(f(n))
