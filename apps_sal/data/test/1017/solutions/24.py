n = int(input())
if n % 3 == 0:
    print(n // 3 * 2)
elif n < 3:
    print(1)
else:
    print(n // 3 * 2 + 1)
