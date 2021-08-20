for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    if n <= 2:
        print(1)
    elif (n - 2) % x == 0:
        print((n - 2) // x + 1)
    else:
        print((n - 2) // x + 2)
