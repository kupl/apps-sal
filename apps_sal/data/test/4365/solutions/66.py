n = int(input())
if n % 2 == 0:
    print(n ** 2 // 4)
else:
    print((n - 1) // 2 * ((n + 1) // 2))
