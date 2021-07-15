for _ in range(int(input())):
    n, x, a, b = list(map(int, input().split()))
    print(min(n - 1, x + abs(a - b)))

