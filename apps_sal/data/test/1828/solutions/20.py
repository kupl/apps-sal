n = int(input())
points = []
ans = 0
for i in range(n):
    x1, y1 = (int(i) for i in input().split())
    points += [[x1, y1]]
for i in range(n):
    x1 = points[i][0]
    y1 = points[i][1]
    x2 = points[(i + 1) % n][0]
    y2 = points[(i + 1) % n][1]
    x3 = points[(i + 2) % n][0]
    y3 = points[(i + 2) % n][1]
    if y1 == y2:
        if x2 > x1:
            if y3 > y2:
                ans += 1

        else:
            if y3 < y2:
                ans += 1
    else:
        if y2 > y1:
            if x3 < x2:
                ans += 1
        else:
            if x2 < x3:
                ans += 1


print(ans)
