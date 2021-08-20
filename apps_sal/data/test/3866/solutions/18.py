n = int(input())
if n % 2 == 0:
    print(-1)
else:
    for i in range(2):
        for j in range(n):
            print(j, end=' ')
        print()
    for i in range(n):
        print(2 * i % n, end=' ')
