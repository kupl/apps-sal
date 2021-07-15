n = int(input())
points = []
flag = False
x1, x2 = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    points.append((a, b))


p = []

for i in range(n):
    p.append((points[i][0] * x1 + points[i][1], points[i][0] * x2 + points[i][1]))

p.sort()
for i in range(n - 1):
    if p[i][0] != p[i + 1][0]:
        if p[i][1] > p[i + 1][1]:
            flag = True
if flag:
    print('YES')
else:
    print('NO')
