from sys import stdin
import math

N = int(stdin.readline())

a = []

for n in range(N):
    x, y = map(int, stdin.readline().split())

    a.append((math.atan2(y, x) + 2 * math.pi) % (2 * math.pi))

a.sort()
a.append(a[0] + 2 * math.pi)

max_gap = max(a[i] - a[i - 1] for i in range(1, len(a)))
print(360 - 180 * max_gap / math.pi)
