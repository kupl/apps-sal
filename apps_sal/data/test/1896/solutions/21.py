def s(n):
    a1 = 0
    n += 1
    d = 6
    an = a1 + d * (n - 1)
    return (a1 + an) // 2 * n


print(s(int(input())) + 1)
