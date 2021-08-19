for _ in range(int(input())):
    n = int(input())
    i = 2
    g = -1
    while i * i <= n:
        if n % i == 0:
            g = n // i
            break
        i += 1
    if g == -1:
        print(1, n - 1)
    else:
        v = n // g - 1
        print(g, g * v)
