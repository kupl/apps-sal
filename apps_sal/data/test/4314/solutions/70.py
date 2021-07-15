h, w = map(int, input().split())

grid = []
for _ in range(h):
    x = input()
    if x.count(".") != len(x):
        grid.append(x)

grid = list(map(list, zip(*grid)))

grid_t = []
for g in grid:
    if g.count(".") != len(g):
        grid_t.append(g)

ans = list(map(list, zip(*grid_t)))

for a in ans:
    print("".join(a))
