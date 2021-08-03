t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        x = n // 2
        for i in range(x):
            print(1, end='')
    else:
        x = n // 2
        x -= 1
        print(7, end='')
        for i in range(x):
            print(1, end='')
    print()
