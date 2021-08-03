n, m = map(int, input().split())

ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

cd = []
for i in range(m):
    cd.append(list(map(int, input().split())))

ans = [0] * m
for i in range(n):
    a, b = ab[i][0], ab[i][1]
    dist = [0] * m
    for j in range(m):
        dist[j] = abs(a - cd[j][0]) + abs(b - cd[j][1])
    dm = min(dist)
    for j in range(m):
        if dist[j] == dm:
            print(j + 1)
            break
