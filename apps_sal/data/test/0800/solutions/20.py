import sys, math

n = int(sys.stdin.readline())
points = []
for i in range(n):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    points.append(math.atan2(a,b))
points = sorted(points)
diffs = []
for i in range(n):
    if (i == n-1):
        diffs.append(points[0]-points[n-1] + 2 * math.pi)
    else:
        diffs.append(points[i+1]-points[i])
print(360-180*max(diffs)/math.pi)
