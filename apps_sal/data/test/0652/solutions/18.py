from sys import stdin, stdout

n = int(stdin.readline())
points = []

for i in range(n):
    x, y = map(int, stdin.readline().split())
    points.append((x, y))

points.sort()
pair = {}

for i in range(n):
    for j in range(i + 1, n):
        if (points[j][0] - points[i][0], points[j][1] - points[i][1]) not in pair:
            pair[(points[j][0] - points[i][0], points[j][1] - points[i][1])] = 1
        else:
            pair[(points[j][0] - points[i][0], points[j][1] - points[i][1])] += 1

ans = 0
for v in pair:
    ans += pair[v] * (pair[v] - 1) // 2

stdout.write(str(ans // 2))
