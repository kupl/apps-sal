for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    x += b - a
    y += d - c
    valid = x1 <= x <= x2 and y1 <= y <= y2
    if x1 == x2: valid &= a == 0 and b == 0
    if y1 == y2: valid &= c == 0 and d == 0

    print(["No", "Yes"][valid])
