(A, B) = map(int, input().split())
grid = []
for _ in range(50):
    grid.append(['#'] * 100)
for _ in range(50):
    grid.append(['.'] * 100)
(div, mod) = divmod(A - 1, 50)
for d in range(div):
    h = 0 + d * 2
    for w in range(0, 100, 2):
        grid[h][w] = '.'
if mod:
    h = 0 + div * 2
    for w in range(0, mod * 2, 2):
        grid[h][w] = '.'
(div, mod) = divmod(B - 1, 50)
for d in range(div):
    h = 51 + d * 2
    for w in range(0, 100, 2):
        grid[h][w] = '#'
if mod:
    h = 51 + div * 2
    for w in range(0, mod * 2, 2):
        grid[h][w] = '#'
print(100, 100)
for g in grid:
    print(''.join(g))
