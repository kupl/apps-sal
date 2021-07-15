n = int(input())
if n % 2 == 1 or n == 2 or n == 4:
    print(0)
elif n % 4 == 2:
    print(n // 4)
else:
    print(n // 4 - 1)

