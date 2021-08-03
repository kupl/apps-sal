def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 2) + n


n = int(input())
print(f(n))
