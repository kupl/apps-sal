import math
N = int(input())
angles = []
for _ in range(N):
    (x, y) = map(int, input().split())
    angles.append(math.atan2(y, x))
angles.sort()
max_angle = 0
for i in range(N):
    angle = abs(angles[i] - angles[(i + 1) % N])
    if i == N - 1:
        angle = 2 * math.pi - angle
    max_angle = max(max_angle, angle)
print(360.0 - max_angle * 180 / math.pi)
