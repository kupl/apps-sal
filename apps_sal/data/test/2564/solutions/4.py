for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    i = 0
    while a <= n and b <= n:
        if a < b: a, b = b, a
        b += a
        i += 1 
    print(i)

