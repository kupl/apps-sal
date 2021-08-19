import math
(w, h, alpha) = list(map(lambda x: int(x), input().split(' ')))
if alpha > 90:
    alpha = 180 - alpha
if alpha == 0:
    print(w * h)
elif alpha == 90:
    print(min(w, h) ** 2)
else:
    limit = 2 * math.degrees(math.atan(h / w))
    if limit > 90:
        limit = 180 - limit
    c = math.cos(math.radians(alpha))
    s = math.sin(math.radians(alpha))
    if alpha >= limit:
        print(min(w, h) ** 2 / s)
    else:
        print(w * h - (c - 1) * (4 * w * h * s - 2 * (w ** 2 + h ** 2)) / (4 * s * c))
