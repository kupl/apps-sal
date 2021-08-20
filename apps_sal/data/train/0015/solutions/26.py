for _ in range(int(input())):
    (a, b, x, y) = map(int, input().split())
    total = a * b
    left = x * b
    right = total - left - b
    down = a * y
    up = total - down - a
    print(max(left, right, down, up))
