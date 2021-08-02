n = int(input())
if n == 2:
    print(1)
    print(2)
elif n % 2 == 0:
    print(n // 2)
    for i in range(n // 2):
        print(2, end=" ")
else:
    print(n // 2)
    n -= 3
    print(3, end=" ")
    for i in range(n // 2):
        print(2, end=" ")
