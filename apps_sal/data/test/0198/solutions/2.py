n = int(input())
p = n // 2
if (n % 2 == 1):
    print(0)
else:
    if (n % 4 == 0):
        print((p - 1) // 2)
    else:
        print(p // 2)
