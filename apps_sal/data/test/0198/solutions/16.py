n = int(input())
if n % 2 == 1:
    print(0)
elif n // 2 % 2 == 1:
    print((n // 2 - 1) // 2)
else:
    print(n // 4 - 1)
