try:
    (m, n) = map(int, input().split())
    while n != 0:
        if m % 10 == 0:
            m = m // 10
        else:
            m -= 1
        n -= 1
    print(m)
except EOFError:
    pass
