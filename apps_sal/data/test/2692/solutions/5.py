for _ in range(int(input())):
    (n, b) = [int(x) for x in input().split()]
    print(n - int((n - 1) / b))
