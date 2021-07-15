n, m = list(map(int, input().split()))
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

cd = []
for i in range(m):
    cd.append(list(map(int, input().split())))

for i in range(n):
    a, b = ab[i]
    dis = 10 ** 9
    point = 0
    for j in range(m):
        c, d = cd[j]
        if abs(a - c) + abs(b - d) < dis:
            point = j + 1
            dis = abs(a - c) + abs(b - d)
    print(point)

