import math
eps = 0.001


def dis(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


def getArea(p1, p2, p3):
    A = p1[0] - p2[0]
    B = p1[1] - p2[1]
    x = (p3[0] * A * A + p3[1] * A * B + p1[0] * B * B - p1[1] * A * B) / (A * A + B * B)
    y = (p1[1] - p2[1]) * (x - p1[0]) / (p1[0] - p2[0]) + p1[1]
    p4 = (x, y)
    return 0.5 * dis(p1, p2) * dis(p3, p4)


def main():
    (x1, y1, x2, y2, x3, y3, x4, y4) = list(map(int, input().split(' ')))
    minX = min(x1, x2, x3, x4)
    maxX = max(x1, x2, x3, x4)
    minY = min(y1, y2, y3, y4)
    maxY = max(y1, y2, y3, y4)
    (x1, y1, x2, y2, x3, y3, x4, y4) = list(map(int, input().split(' ')))
    square_area = dis((x1, y1), (x2, y2)) * dis((x1, y1), (x2, y2))
    for i in range(minX, maxX + 1):
        for j in range(minY, maxY + 1):
            area1 = getArea((x1, y1), (x2, y2), (i, j))
            area2 = getArea((x2, y2), (x3, y3), (i, j))
            area3 = getArea((x3, y3), (x4, y4), (i, j))
            area4 = getArea((x4, y4), (x1, y1), (i, j))
            if area1 + area2 + area3 + area4 - square_area < eps:
                print('YES')
                return
    print('NO')


main()
