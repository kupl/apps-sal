for TT in range(1, int(input()) + 1):
    k, n, a, b = map(int, input().split())
    x = (k - n * b + (a - b - 1)) // (a - b) - 1
    x = min(x, n)
    x = max(x, -1)
    print(x)
