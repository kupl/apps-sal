
face = set('face')
n, m = list(map(int, input().split()))
faces = []
for i in range(n):
    faces.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        dxdy = [(0, 0), (0, 1), (1, 1), (1, 0)]
        f = []
        for dx, dy in dxdy:
            if 0 <= dy + i < n and 0 <= dx + j < m:
                f.append(faces[i + dy][j + dx])
        if face == set(f):
            count += 1
print(count)
