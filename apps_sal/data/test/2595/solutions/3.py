for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < m:
        n, m = m, n
    if n % m == 0:
        x = n // m
        b = 0
        while x % 2 == 0:
            x //= 2
            b += 1
        if x != 1:
            print(-1)
        else:
            print((b + 2) // 3)
    else:
        print(-1)
