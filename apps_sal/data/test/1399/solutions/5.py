"""
Created on Tue Sep 18 10:09:57 2018

@author: a.teffal

Chalenge :  Covered Points
"""
from math import gcd


def covered_points(xa, ya, xb, yb):
    """
    assumes all parameters are integers
    Returns the covered points by the segement A-B having integer 
    coordinates

    """
    if xb < xa:
        temp_x = xa
        xa = xb
        xb = temp_x
        temp_y = ya
        ya = yb
        yb = temp_y
    y_0 = abs(yb - ya)
    x_0 = xb - xa
    return gcd(y_0, x_0) + 1


def intersection2(xa, ya, xb, yb, xc, yc, xd, yd):
    if max(xa, xb) < min(xc, xd):
        return ()
    if max(ya, yb) < min(yc, yd):
        return ()
    if xa == xb and xc == xd or (ya == yb and yc == yd):
        return ()
    if ya == yb and yc == yd:
        return ()
    a1 = yb - ya
    b1 = xb - xa
    c1 = xa * a1 - ya * b1
    a2 = yd - yc
    b2 = xd - xc
    c2 = xc * a2 - yc * b2
    det = a1 * b2 - a2 * b1
    if det == 0:
        return ()
    detx = c1 * b2 - c2 * b1
    dety = -a1 * c2 + a2 * c1
    if detx % det != 0 or dety % det != 0:
        return ()
    x = int(detx / det)
    y = int(dety / det)
    if x < min(xa, xb) or x > max(xa, xb) or x < min(xc, xd) or (x > max(xc, xd)):
        return ()
    if y < min(ya, yb) or y > max(ya, yb) or y < min(yc, yd) or (y > max(yc, yd)):
        return ()
    return (x, y)


def __starting_point():
    n = int(input())
    Ax = [0] * n
    Ay = [0] * n
    Bx = [0] * n
    By = [0] * n
    n_cov = 0
    intersections = {}
    for i in range(n):
        line = input().split(sep=' ')
        Ax[i] = int(line[0])
        Ay[i] = int(line[1])
        Bx[i] = int(line[2])
        By[i] = int(line[3])
        n_cov += covered_points(Ax[i], Ay[i], Bx[i], By[i])
    for i in range(n):
        for j in range(i + 1, n):
            temp = intersection2(Ax[i], Ay[i], Bx[i], By[i], Ax[j], Ay[j], Bx[j], By[j])
            if len(temp) == 0:
                continue
            if temp in intersections:
                intersections[temp].append(i)
                intersections[temp].append(j)
            else:
                intersections[temp] = [i, j]
    for i in intersections:
        n_cov = n_cov - len(set(intersections[i])) + 1
    print(n_cov)


__starting_point()
