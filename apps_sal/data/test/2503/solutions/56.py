N, K = map(int, input().split())

score = [[0] * (K + 1) for y in range(K + 1)]
base_hope = 0

for i in range(N):
    x, y, c = input().split()
    x2, y2 = int(x) // K, int(y) // K
    x_coord, y_coord = int(x) % K + 1, int(y) % K + 1
    if ((x2 + y2) % 2 == 0 and c == "W") or ((x2 + y2) % 2 == 1 and c == "B"):
        score[y_coord][x_coord] += 1
        base_hope += 1
    else:
        score[y_coord][x_coord] -= 1

xy = [(x, y) for x in range(K) for y in range(K)]
for x, y in xy:
    score[y + 1][x + 1] += score[y + 1][x] + score[y][x + 1] - score[y][x]

max_hope = 0
for x, y in xy:
    hope = base_hope - score[K][x] - score[y][K] + 2 * score[y][x]
    true_hope = hope if hope > N - hope else N - hope
    if true_hope > max_hope:
        max_hope = true_hope

print(max_hope)
