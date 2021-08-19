n = int(input().strip())
if n % 2 == 1:
    print((n + 1) // 2 % 2)
    print((n + 1) // 2, end=' ')
    i = 1
    while i <= n:
        if i < n:
            print(i, i + 1, end=' ')
        else:
            print(i, end=' ')
        i += 4
    print()
else:
    print(n // 2 % 2)
    print(n // 2, 1, end=' ')
    i = 4
    while i <= n:
        if i < n:
            print(i, i + 1, end=' ')
        else:
            print(i, end=' ')
        i += 4
    print()
