""" Peter and Snow Blower """
import math


def cross(vecA, vecB):
    return abs(vecA[0] * vecB[1] - vecA[1] * vecB[0])


def l2_norm(pointA, pointB):
    return (pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2


def height5(P, A, B):
    a = l2_norm(A, P)
    b = l2_norm(B, P)
    base = l2_norm(A, B)
    if a >= base + b or b >= base + a:
        return min(a, b)
    else:
        vecA = (A[0] - P[0], A[1] - P[1])
        vecB = (B[0] - P[0], B[1] - P[1])
        area = cross(vecA, vecB)
        h = area * area / base
        return h


def CF613A():
    (N, cx, cy) = list(map(int, input().split()))
    points = [tuple(map(int, input().split())) for _ in range(N)]
    center = (cx, cy)
    distances = [l2_norm(center, point) for point in points]
    max_radius = max(distances)
    min_radius = float('inf')
    for i in range(N):
        height = height5(center, points[i], points[(i + 1) % N])
        min_radius = min(min_radius, height)
    area = math.pi * (max_radius - min_radius)
    return area


def __starting_point():
    res = CF613A()
    print(res)


__starting_point()
