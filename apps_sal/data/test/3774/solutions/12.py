(n, m) = map(int, input().split())
if n > m:
    (n, m) = (m, n)
if n == 1:
    print(m // 6 * 6 + max(m % 6 * 2 - 6, 0))
elif n == 2:
    if m == 2:
        print(0)
    elif m == 3 or m == 7:
        print(m * 2 - 2)
    else:
        print(m * 2)
else:
    print(n * m // 2 * 2)
