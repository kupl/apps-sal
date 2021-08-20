(a, b) = [int(x) for x in input().split()]
(c, d) = [int(x) for x in input().split()]


def isCrossing(square1, square2):
    for vert in square1:
        if vert[0] == 0 or vert[1] == 0:
            return True
        if square2[0][1] <= vert[1] * square2[0][0] / vert[0] <= square2[1][1]:
            return True
        if square2[0][0] <= vert[0] * square2[0][1] / vert[1] <= square2[3][0]:
            return True
        if square2[3][1] <= vert[1] * square2[2][0] / vert[0] <= square2[2][1]:
            return True
        if square2[1][0] <= vert[0] * square2[1][1] / vert[1] <= square2[2][0]:
            return True
    for vert in square2:
        if vert[0] == 0 or vert[1] == 0:
            return True
        if square1[0][1] <= vert[1] * square1[0][0] / vert[0] <= square1[1][1]:
            return True
        if square1[0][0] <= vert[0] * square1[0][1] / vert[1] <= square1[3][0]:
            return True
        if square1[3][1] <= vert[1] * square1[2][0] / vert[0] <= square1[2][1]:
            return True
        if square1[1][0] <= vert[0] * square1[1][1] / vert[1] <= square1[2][0]:
            return True
    return False


def binSearch(left, right, a, b, c, d):
    m = (left + right) / 2
    eps = 10 ** (-10)
    while abs(m - left) > eps and abs(right - m) > eps:
        if isCrossing(([a - m, b - m], [a - m, b + m], [a + m, b + m], [a + m, b - m]), ([c - m, d - m], [c - m, d + m], [c + m, d + m], [c + m, d - m])):
            right = m
        else:
            left = m
        m = (left + right) / 2
    return m


print(binSearch(10 ** (-10), 2 * 10 ** 9, a, b, c, d))
