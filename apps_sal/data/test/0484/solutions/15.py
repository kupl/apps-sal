n, a, b = map(int, input().split())
l = [[int(j) for j in input().split()] for i in range(n)]
ms = 0
for i in range(n):
    for j in range(i + 1, n):
        if l[i][0] + l[j][0] <= a and max(l[i][1], l[j][1]) <= b:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][1] + l[j][1] <= a and max(l[i][0], l[j][0]) <= b:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][0] + l[j][1] <= a and max(l[i][1], l[j][0]) <= b:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][1] + l[j][0] <= a and max(l[i][0], l[j][1]) <= b:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][0] + l[j][0] <= b and max(l[i][1], l[j][1]) <= a:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][1] + l[j][1] <= b and max(l[i][0], l[j][0]) <= a:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][0] + l[j][1] <= b and max(l[i][1], l[j][0]) <= a:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
        if l[i][1] + l[j][0] <= b and max(l[i][0], l[j][1]) <= a:
            ms = max(ms, l[i][0] * l[i][1] + l[j][0] * l[j][1])
print(ms)
