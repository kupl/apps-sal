(n, h, a, b, k) = map(int, input().split())
for i in range(k):
    (y1, x1, y2, x2) = map(int, input().split())
    if y1 == y2:
        print(abs(x1 - x2))
    elif x1 <= b and x2 >= a or (x1 >= a and x2 <= b):
        print(abs(y1 - y2) + abs(x1 - x2))
    elif x1 >= a:
        print(abs(y1 - y2) + abs(x1 - b) + abs(x2 - b))
    elif x1 <= a:
        print(abs(y1 - y2) + abs(x1 - a) + abs(x2 - a))
