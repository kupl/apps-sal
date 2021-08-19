(n, k) = map(int, input().split())
if k > 2:
    if k % 2 == 0:
        a = n // (k // 2)
        if a % 2 == 0:
            print(2 * (a // 2) ** 3)
        else:
            print((a // 2) ** 3 + (a // 2 + 1) ** 3)
    else:
        print((n // k) ** 3)
elif k == 2:
    if n % 2 == 0:
        print(2 * (n // 2) ** 3)
    else:
        print((n // 2) ** 3 + (n // 2 + 1) ** 3)
else:
    print(n ** 3)
