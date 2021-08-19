import math


def rst(A, B):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


(a, b, c) = list(map(float, input().split()))
(x1, y1, x2, y2) = list(map(float, input().split()))
l = []
if a == 0 or b == 0:
    print(abs(x2 - x1) + abs(y1 - y2))
else:
    st = (x1, y1)
    fn = (x2, y2)
    xa = x1
    ya = (-c - a * x1) / b
    A = (xa, ya)
    xb = x2
    yb = (-c - a * x2) / b
    B = (xb, yb)
    xc = (-c - b * y1) / a
    yc = y1
    C = (xc, yc)
    xd = (-c - b * y2) / a
    yd = y2
    D = (xd, yd)
    print(min(abs(x2 - x1) + abs(y1 - y2), rst(st, A) + rst(A, B) + rst(B, fn), rst(st, A) + rst(A, D) + rst(D, fn), rst(st, C) + rst(C, B) + rst(B, fn), rst(st, C) + rst(C, D) + rst(D, fn)))
