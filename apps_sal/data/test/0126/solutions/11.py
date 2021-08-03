a = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
d = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
n = int(input())
b = list(map(int, list(input())))
c = []
for i in range(n - 1):
    c.append((d[b[i + 1]][0] - d[b[i]][0], d[b[i + 1]][1] - d[b[i]][1]))
for i in range(10):
    x, y = d[i][0], d[i][1]
    fl = 1
    for j in c:
        x1, y1 = x + j[0], y + j[1]
        if (x1, y1) not in d:
            fl = 0
        x, y = x1, y1
    if fl and i != b[0]:
        print("NO")
        break
else:
    print("YES")
