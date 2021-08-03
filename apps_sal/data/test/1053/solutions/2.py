def f(n):
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return 2 * f(n // 2) + n // 2
    else:
        return 2 * f(n // 2 + 1) + n // 2


n = int(input())
print(f(n))
