f = lambda: map(int, input().split())
n, m, s, d = f()
p, x, z = [], -1, 1
for y in sorted(f()) + [m + 1]:
    if y - x > s + 1 or y > m or x < 0:
        u = x - z + 2
        v = y - x - 2
        if u > d or v < s and x < 0:
            p = ['IMPOSSIBLE']
            break
        if u: p += ['JUMP ' + str(u)]
        if v: p += ['RUN ' + str(v)]
        z = y
    x = y
print('\n'.join(p))
