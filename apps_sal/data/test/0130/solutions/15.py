n, m = map(int, input().split())
pole = list()
min_i, min_j, max_i, max_j = n, m, -1, -1
count_B = 0

for i in range(n):
    pole += [input()]
    for j in range(m):
        t = pole[i][j]
        if t == 'B':
            count_B += 1
            min_i, min_j, max_i, max_j = min(i, min_i), min(j, min_j), max(i, max_i), max(j, max_j)

d_i, d_j = max_i - min_i, max_j - min_j
side = max(d_i + 1, d_j + 1)

print(1) if count_B == 0 else print(side ** 2 - count_B) if side <= min(n, m) else print(-1)
