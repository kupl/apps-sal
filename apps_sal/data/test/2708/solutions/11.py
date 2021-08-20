try:
    (n, k) = map(int, input().split())
    m = n
    c = 0
    while m != 0:
        m = m // 10
        c += 1
    for _ in range(k):
        if c == 1:
            n = n - 1
            if n == 0:
                break
        elif n % 10 != 0:
            n = n - 1
        elif n % 10 == 0:
            n = n // 10
        elif n == 0:
            break
    print(n)
except:
    pass
