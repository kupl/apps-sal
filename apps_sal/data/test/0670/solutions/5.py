import math

a, b, c = [float(i) for i in input().split()]
xy = [float(i) for i in input().split()]
A = [xy[0], xy[1]]
B = [xy[2], xy[3]]

distances = []


def get_distance(K, M):
    return math.sqrt((K[0] - M[0]) * (K[0] - M[0]) + (K[1] - M[1]) * (K[1] - M[1]))


def get_point_h(K):
    x = (-b * K[1] - c) / a
    point = (x, K[1])
    distance = get_distance(K, point)
    return point, distance


def get_point_v(K):
    y = (-a * K[0] - c) / b
    point = (K[0], y)
    distance = get_distance(K, point)
    return point, distance


manhatten_distance = abs(A[0] - B[0]) + abs(A[1] - B[1])

distances.append(manhatten_distance)

if a != 0:
    p1, d1 = get_point_h(A)
    p3, d3 = get_point_h(B)
    distances.append(get_distance(p1, p3) + d1 + d3)

if b != 0:
    p2, d2 = get_point_v(A)
    p4, d4 = get_point_v(B)
    distances.append(get_distance(p2, p4) + d2 + d4)

if a != 0 and b != 0:
    distances.append(get_distance(p2, p3) + d2 + d3)
    distances.append(get_distance(p1, p4) + d1 + d4)

print(min(distances))
