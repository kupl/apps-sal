def pos(x, y):
    if y & 1:
        return y * w + w - 1 - x
    return y * w + x


CUBE = 6
h, w = 10, 10
n = h * w

grid = []
for y in range(h):
    line = list(map(int, input().split()))
    grid.append(line)
grid.reverse()

to = [0] * n
for y in range(h):
    for x in range(w):
        y1 = y + grid[y][x]
        if y1 != y:
            to[pos(x, y)] = pos(x, y + grid[y][x])

exp = [0] * (n + CUBE)
for i in range(n - 2, -1, -1):
    exp[i] = 1
    for j in range(1, CUBE + 1):
        exp_to = exp[i + j] / CUBE
        if i + j < n and to[i + j]:
            exp_to = min(exp_to, exp[to[i + j]] / CUBE)
        exp[i] += exp_to
    if i + CUBE >= n:
        exp[i] = CUBE * exp[i] / (n - 1 - i)
print(f"{exp[0]:.16f}")
