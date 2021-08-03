n = int(input())
if n == 2:
    print(1)
else:
    print(2 * (n // 3) + (1 if n % 3 != 0 else 0))
