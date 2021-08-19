for _ in range(int(input())):
    n = int(input())
    if n % 2:
        print('7', end='')
        n -= 3
    while n:
        print('1', end='')
        n -= 2
    print()
