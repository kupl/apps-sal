for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    x, y, z = list(map(int, input().split()))
    print(2 * min(c, y) - 2 * max(0, min(z - max(c - y, 0) - a, b)))
