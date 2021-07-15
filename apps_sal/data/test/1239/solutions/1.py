3
import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]

a.sort()

count = 0
dist = float('inf')

for i in range(n - 1):
    d = a[i + 1] - a[i]
    if d < dist:
        dist = d
        count = 1
    elif d == dist:
        count += 1

print(dist, count)
