for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    if n <= 2:
        print(1)
    else:
        n -= 3
        print(n // x + 2)
