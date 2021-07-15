r, c, n, k = list(map(int, input().split()))
alt = []
count = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    alt.append([a - 1, b - 1])
for x1 in range(r):
    for x2 in range(x1 + 1):
        for y1 in range(c):
            for y2 in range(y1 + 1):
                d = 0
                for i in range(n):
                    if (alt[i][0] <= x1 and alt[i][0] >= x2 and alt[i][1] <= y1 and alt[i][1] >= y2):
                        d += 1
                if d >= k:
                    count += 1
print(count)
