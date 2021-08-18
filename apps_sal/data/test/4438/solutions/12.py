from collections import defaultdict
n = int(input())
points = defaultdict(list)
points[0].append((0, 0))
for i in range(n):
    x, y = list(map(int, input().split()))
    points[max(x, y)].append((x, y))
for level in points:
    points[level].sort(key=lambda x: (x[0], -x[1]))
levels = sorted(points.keys())
dp = [[0, 0] for i in levels]
def dist(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])


for i in range(1, len(levels)):
    start = points[levels[i]][0]
    end = points[levels[i]][-1]
    prevstart = points[levels[i - 1]][0]
    prevend = points[levels[i - 1]][-1]
    dp[i][0] = min(dp[i - 1][0] + dist(prevstart, end), dp[i - 1][1] + dist(prevend, end)) + dist(start, end)
    dp[i][1] = min(dp[i - 1][0] + dist(prevstart, start), dp[i - 1][1] + dist(prevend, start)) + dist(start, end)
print(min(dp[-1]))
