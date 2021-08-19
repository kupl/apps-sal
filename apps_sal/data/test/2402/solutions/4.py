for _ in range(int(input())):
    (n, x, y) = list(map(int, input().split()))
    print(min(max(x + y + 1 - n, 1), n), min(n, x + y - 1))
