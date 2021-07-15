for _ in range(int(input())):
    x, y, n = list(map(int, input().split()))
    z = (n - y) // x
    print(x * z + y)
