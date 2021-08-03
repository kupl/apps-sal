points = []
for i in range(3):
    points.append(tuple(map(int, input().split())))

ans = set()
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        vector = (points[j][0] - points[i][0], points[j][1] - points[i][1])
        third = 0 + 1 + 2 - i - j
        ans.add((points[third][0] + vector[0], points[third][1] + vector[1]))

print(len(ans))
for a, b in ans:
    print(a, b)
