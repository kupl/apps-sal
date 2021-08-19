def f():
    return [*map(int, input().split())]


(h, w) = f()
g = [f() for _ in range(h)]
tx = ty = 0
a = []
for y in range(h):
    for x in range(w):
        if y % 2:
            if tx:
                (nx, ny) = (tx - 1, ty)
            else:
                (nx, ny) = (tx, ty + 1)
        elif tx < w - 1:
            (nx, ny) = (tx + 1, ty)
        else:
            (nx, ny) = (tx, ty + 1)
        if ny == h:
            break
        if g[ty][tx] % 2:
            g[ty][tx] -= 1
            g[ny][nx] += 1
            a += [[ty + 1, tx + 1, ny + 1, nx + 1]]
        (ty, tx) = (ny, nx)
    if ny == h:
        break
print(len(a))
for l in a:
    print(*l)
