import math
(x1, y1, x2, y2) = tuple((int(i) for i in input().split()))
V = [[0 for j in range(10)] for i in range(10)]


def black(x, y):
    if x % 2 == 1:
        return y % 2 == 1
    else:
        return y % 2 == 0


a = 2
b = 0
c = 0
if x1 == x2:
    a -= 1
if y1 == y2:
    a -= 1
if abs(x1 - x2) == abs(y1 - y2):
    b = 1
elif black(x1, y1) == black(x2, y2):
    b = 2
else:
    b = 0
c = max(abs(x1 - x2), abs(y1 - y2))
print(a, b, c)
