def y():
    return int(input())


for _ in range(y()):
    n = y()
    c = 0
    while 2 ** (2 * c + 1) - 2 ** c <= n:
        n -= 2 ** (2 * c + 1) - 2 ** c
        c += 1
    print(c)
