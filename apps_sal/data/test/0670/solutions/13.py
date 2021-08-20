(a, b, c) = map(int, input().split())
(x1, y1, x2, y2) = map(int, input().split())
if a != 0 and b != 0:
    x1_ = -1 * (b * y1 + c) / a
    y1_ = -1 * (a * x1 + c) / b
    x2_ = -1 * (b * y2 + c) / a
    y2_ = -1 * (a * x2 + c) / b
    p1 = abs(x1 - x1_) + abs(y2 - y2_) + ((x1_ - x2) ** 2 + (y1 - y2_) ** 2) ** 0.5
    p2 = abs(x1 - x1_) + abs(x2 - x2_) + ((x1_ - x2_) ** 2 + (y1 - y2) ** 2) ** 0.5
    p3 = abs(y1 - y1_) + abs(y2 - y2_) + ((x1 - x2) ** 2 + (y1_ - y2_) ** 2) ** 0.5
    p4 = abs(y1 - y1_) + abs(x2 - x2_) + ((x1 - x2_) ** 2 + (y1_ - y2) ** 2) ** 0.5
    p5 = abs(y1 - y2) + abs(x2 - x1)
    sp = [p1, p2, p3, p4, p5]
    print(min(sp))
else:
    print(abs(y1 - y2) + abs(x2 - x1))
