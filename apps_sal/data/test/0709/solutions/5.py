def f(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return f(n // 2) + 1
    else:
        return f(n // 2)


n = int(input())
print(f(n))
