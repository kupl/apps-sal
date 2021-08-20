points = [tuple((int(x) for x in input().split())) for _ in range(3)]
points.sort()
(p1, p2, p3) = points
if p1[0] == p2[0] and p2[0] == p3[0] or (p1[1] == p2[1] and p2[1] == p3[1]):
    print(1)
elif p1[0] == p2[0]:
    if min(p1[1], p2[1]) < p3[1] < max(p1[1], p2[1]):
        print(3)
    else:
        print(2)
elif p2[0] == p3[0]:
    if min(p2[1], p3[1]) < p1[1] < max(p2[1], p3[1]):
        print(3)
    else:
        print(2)
else:
    points.sort(key=lambda p: p[1])
    if p1[1] == p2[1]:
        if min(p1[0], p2[0]) < p3[0] < max(p1[0], p2[0]):
            print(3)
        else:
            print(2)
    elif p2[1] == p3[1]:
        if min(p2[0], p3[0]) < p1[0] < max(p1[0], p2[0]):
            print(3)
        else:
            print(2)
    else:
        print(3)
