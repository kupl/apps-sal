from math import atan2, pi

def solve():
    n = int(input().rstrip())
    angles = []
    for _ in range(n):
        a, b = list(map(int, input().rstrip().split()))
        angles.append(atan2(b, a))
    angles.sort()
    maxangle = 2 * pi - (angles[n - 1] - angles[0])
    for i in range(n - 1):
        maxangle = max(angles[i + 1] - angles[i], maxangle)
    return 360 - maxangle * 180 / pi

def __starting_point():
    print(solve())

__starting_point()
