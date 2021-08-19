from itertools import product
(h, w, k) = list(map(int, input().split()))
grid = []
for i in range(h):
    grid.append(input())
pattern = list(product((0, 1), repeat=h + w))
result = 0
for p in range(len(pattern)):
    p_h = pattern[p][:h]
    p_w = pattern[p][h:]
    cnt = 0
    for i in range(h):
        if p_h[i] == 0:
            for j in range(w):
                if p_w[j] == 0:
                    now = grid[i][j]
                    if now == '#':
                        cnt += 1
    if cnt == k:
        result += 1
print(result)
