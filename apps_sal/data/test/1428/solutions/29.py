
N, C = list(map(int, input().split()))

D = [[0] * C for i in range(C)]
for i in range(C):
    D[i] = list(map(int, input().split()))


groups = [[0] * C for i in range(3)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        groups[(i + j) % 3][line[j] - 1] += 1

pattern = [[[0] * 2 for j in range(C)] for i in range(3)]

for i in range(len(groups)):
    for j in range(C):
        iwakan = 0
        for k in range(len(groups[i])):
            iwakan += groups[i][k] * D[k][j]
        pattern[i][j][0] = iwakan
        pattern[i][j][1] = j

for i in range(len(pattern)):
    pattern[i] = sorted(pattern[i], key=lambda x: x[0])

ans = 10 ** 9 + 7
for a in range(3):
    for b in range(3):
        if pattern[0][a][1] == pattern[1][b][1]:
            continue
        for c in range(3):
            if pattern[0][a][1] == pattern[2][c][1]:
                continue
            if pattern[1][b][1] == pattern[2][c][1]:
                continue
            val = pattern[0][a][0] + pattern[1][b][0] + pattern[2][c][0]
            if val < ans:
                ans = val
print(ans)
