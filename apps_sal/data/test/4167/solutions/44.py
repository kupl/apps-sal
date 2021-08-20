(n, k) = map(int, input().split())
if k == 1:
    print(n ** 3)
elif k == 2:
    m = n % 2
    o = n // 2
    print((o + m) ** 3 + o ** 3)
elif k % 2 == 1:
    x = n // k
    print(x ** 3)
else:
    x = n // k
    y = n // (k // 2)
    print(x ** 3 + (y - x) ** 3)
