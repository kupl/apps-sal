n = int(input())
if n % 2 == 1:
    for i in range(n):
        print(i, end=" ")
    print()
    for i in range(n):
        print((i + 1)%n, end=" ")
    print()
    for i in range(n):
        print((i + (i + 1)%n)%n, end=" ")
else:
    print(-1)
