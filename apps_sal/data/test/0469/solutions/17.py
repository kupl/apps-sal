from math import sqrt
(r, h) = (int(x) for x in input().split(' '))
in_box = 2 * h // r + 1
remainder = h % r + r
height = r * sqrt(3) / 2 + r
if remainder < height:
    print(in_box)
else:
    print(in_box + 1)
