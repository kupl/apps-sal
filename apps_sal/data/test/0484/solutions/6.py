n, a, b = list(map(int, input().split()))

d = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if i != j:
            tmp = d[i][0] * d[i][1] + d[j][0] * d[j][1]
            for x1 in range(2):
                for x2 in range(2):
                    #print(i, j, max(d[i][x1], d[j][x2]), d[i][1 - x1] + d[j][1 - x2])
                    if max(d[i][x1], d[j][x2]) <= b and d[i][1 - x1] + d[j][1 - x2] <= a:
                        ans = max(ans, tmp)
                    if max(d[i][x1], d[j][x2]) <= a and d[i][1 - x1] + d[j][1 - x2] <= b:
                        ans = max(ans, tmp)
print(ans)

