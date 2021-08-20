n = int(input())
p = []
for i in range(n):
    (x, y) = map(int, input().split())
    p.append([x, y])
p = sorted(p)
day = p[0][1]
for i in range(1, n):
    if p[i][1] >= day:
        day = p[i][1]
    else:
        day = p[i][0]
print(day)
