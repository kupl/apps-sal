def f(m, n):
    if len(str(m)) < len(str(n)):
        return f(m, int('9' * (len(str(n)) - 1))) + f(int('9' * (len(str(n)) - 1)) + 1, n)
    else:
        return len(str(n)) * (n - m + 1)


n = int(input())
m = 1
print(f(1, n))
