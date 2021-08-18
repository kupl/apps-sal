x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())
pl = (x2 - x1) * (y2 - y1)


def peresech(a, b, c, d, a2, b2, c2, d2):
    l1 = [a, c, a2, c2]
    l2 = [b, d, b2, d2]
    l1.sort()
    l2.sort()
    if a == a2 and b == b2 and c == c2 and d == d2:
        return [a, b, c, d]
    if b > d2 or c < a2 or d < b2 or a > c2:
        return 0
    return [l1[1], l2[1], l1[2], l2[2]]


l = peresech(x1, y1, x2, y2, x3, y3, x4, y4)
l2 = peresech(x1, y1, x2, y2, x5, y5, x6, y6)
if l == 0:
    if l2 != 0:
        if (l2[2] - l2[0]) * (l2[3] - l2[1]) != pl:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    return
if l2 == 0 and l != 0:
    if (l[2] - l[0]) * (l[3] - l[1]) != pl:
        print("YES")
    else:
        print("NO")
    return
l3 = peresech(l[0], l[1], l[2], l[3], l2[0], l2[1], l2[2], l2[3])
if l3 == 0:
    if (l[2] - l[0]) * (l[3] - l[1]) + (l2[2] - l2[0]) * (l2[3] - l2[1]) == pl:
        print("NO")
    else:
        print("YES")
    return
if (l[2] - l[0]) * (l[3] - l[1]) + (l2[2] - l2[0]) * (l2[3] - l2[1]) - (l3[2] - l3[0]) * (l3[3] - l3[1]) == pl:
    print("NO")
else:
    print("YES")
