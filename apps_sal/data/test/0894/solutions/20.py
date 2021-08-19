(x, y) = map(int, input().split())
(p1, p2) = ((0, (-1 if y < 0 else 1) * (abs(x) + abs(y))), ((-1 if x < 0 else 1) * (abs(x) + abs(y)), 0))
if p1[0] > p2[0]:
    (p1, p2) = (p2, p1)
print(' '.join(map(str, p1 + p2)))
