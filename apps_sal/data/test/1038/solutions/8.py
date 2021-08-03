a, b = map(int, input().split())


def f(n):
    m = n % 4
    if m == 0:
        return n
    if m == 1:
        return 1
    if m == 2:
        return n + 1
    if m == 3:
        return 0


print(f(b) ^ f(a - 1))
