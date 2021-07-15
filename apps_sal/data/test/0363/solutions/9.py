def f(n):
    n1 = n
    r = 0
    t = 0
    for i in range(0, 15):
        if n >= 10 ** i:
            r = r + n - 10 ** i + 1
    return r
n = int(input())
print(f(n))

