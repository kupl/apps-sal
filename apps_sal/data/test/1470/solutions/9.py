n = int(input())
if n <= 6:
    print(1)
elif n % 11 == 0:
    print(2 * (n // 11))
elif n % 11 <= 6:
    print(2 * (n // 11) + 1)
else:
    print(2 * n // 11 + 1)
