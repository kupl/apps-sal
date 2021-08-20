from sys import stdin
import math
N = int(stdin.readline())
angles = []
for n in range(N):
    (x, y) = map(int, stdin.readline().split())
    angles.append((math.atan2(y, x) + 2 * math.pi) % (2 * math.pi))
angles.sort()
angles.append(angles[0] + 2 * math.pi)
max_gap = max((angles[i] - angles[i - 1] for i in range(1, len(angles))))
print(360 - 180 * max_gap / math.pi)
