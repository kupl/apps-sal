N, C = list(map(int, input().split()))

discomforts = [[0] * (N + 1)]
for _ in range(C):
    row = [0]
    row.extend(list(map(int, input().split())))
    discomforts.append(row)
grid = [[0] * (N + 1)]
for _ in range(N):
    row = [0]
    row.extend(list(map(int, input().split())))
    grid.append(row)

color_counts = [[0] * (C + 1) for i in range(3)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        color_counts[(i + j) % 3][grid[i][j]] += 1

ans = float('inf')
for c0 in range(1, C + 1):
    for c1 in range(1, C + 1):
        for c2 in range(1, C + 1):
            if c0 != c1 and c1 != c2 and c2 != c0:
                total = 0
                for i in range(1, C + 1):
                    total += discomforts[i][c0] * color_counts[0][i]
                    total += discomforts[i][c1] * color_counts[1][i]
                    total += discomforts[i][c2] * color_counts[2][i]
                ans = min(ans, total)
print(ans)
