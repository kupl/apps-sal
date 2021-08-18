for i in range(int(input())):
    n, b = list(map(int, input().split()))
    print(1 + n * (b - 1) // b)
