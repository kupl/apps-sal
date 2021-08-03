n = int(input())

if n == 1 or n == 2:
    print(1)
    print(1)
elif n == 3:
    print(2)
    print(1, 3)
elif n == 4:
    print(4)
    print(2, 4, 1, 3)
elif n % 2 == 0:
    print(n)
    for i in range(1, n // 2 + 1):
        print(i, end=" ")
        print(n // 2 + i, end=" ")
else:
    print(n)
    for i in range(1, n // 2 + 1):
        print(i, end=" ")
        print(n // 2 + i + 1, end=" ")
    print(n // 2 + 1)
