n = int(input())
if n % 2 == 1:
    print(0)
elif n % 4 == 0:
    print((n - 1) // 4)
else:
    print(n // 4)
