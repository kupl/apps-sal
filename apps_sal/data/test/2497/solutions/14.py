import sys


def check(t):
    maxx = max(ud_maxx, r_maxx + t, l_maxx - t)
    minx = min(ud_minx, r_minx + t, l_minx - t)
    maxy = max(lr_maxy, u_maxy + t, d_maxy - t)
    miny = min(lr_miny, u_miny + t, d_miny - t)
    return (maxx - minx) * (maxy - miny)


n = int(input())
lr_maxy, lr_miny, ud_maxx, ud_minx = -1e9, 1e9, -1e9, 1e9
l_maxx, l_minx, r_maxx, r_minx = -1e9, 1e9, -1e9, 1e9
u_maxy, u_miny, d_maxy, d_miny = -1e9, 1e9, -1e9, 1e9
for line in sys.stdin:
    x, y, d = line.rstrip().split()
    x, y = int(x), int(y)
    if d == 'L':
        lr_maxy = max(lr_maxy, y)
        lr_miny = min(lr_miny, y)
        l_maxx = max(l_maxx, x)
        l_minx = min(l_minx, x)
    elif d == 'R':
        lr_maxy = max(lr_maxy, y)
        lr_miny = min(lr_miny, y)
        r_maxx = max(r_maxx, x)
        r_minx = min(r_minx, x)
    elif d == 'U':
        ud_maxx = max(ud_maxx, x)
        ud_minx = min(ud_minx, x)
        u_maxy = max(u_maxy, y)
        u_miny = min(u_miny, y)
    else:
        ud_maxx = max(ud_maxx, x)
        ud_minx = min(ud_minx, x)
        d_maxy = max(d_maxy, y)
        d_miny = min(d_miny, y)

inflections = {0}
inflections.add(max(0, l_maxx - ud_maxx))
inflections.add(max(0, (l_maxx - r_maxx) / 2))
inflections.add(max(0, ud_maxx - r_maxx))
inflections.add(max(0, l_minx - ud_minx))
inflections.add(max(0, (l_minx - r_minx) / 2))
inflections.add(max(0, ud_minx - r_minx))

inflections.add(max(0, d_maxy - lr_maxy))
inflections.add(max(0, (d_maxy - u_maxy) / 2))
inflections.add(max(0, lr_maxy - u_maxy))
inflections.add(max(0, d_miny - lr_miny))
inflections.add(max(0, (d_miny - u_miny) / 2))
inflections.add(max(0, lr_miny - u_miny))

print((min(list(map(check, inflections)))))

