n = int(input())
if n % 4 == 0:
    print(0)
    print(n // 2, end=' ')
    step = 0
    for i in range(1, n + 1, 2):
        print(i + step, end=' ')
        step = 1 - step
elif n % 4 == 3:
    print(0)
    print(n // 2, end=' ')
    step = 1
    for i in range(2, n + 1, 2):
        print(i + step, end=' ')
        step = 1 - step
else:
    print(1)
    if n % 4 == 2:
        print(n // 2, end=' ')
        step = 0
        for i in range(1, n + 1, 2):
            print(i + step, end=' ')
            step = 1 - step
    else:
        print(n // 2, end=' ')
        step = 1
        for i in range(2, n + 1, 2):
            print(i + step, end=' ')
            step = 1 - step
