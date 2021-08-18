h, w = list(map(int, input().split()))
f = [input() for y in range(h)]
ly = 0
while 'B' not in f[ly]:
    ly += 1
ry = ly + 1
while ry < h and 'B' in f[ry]:
    ry += 1
lx = 0
while 'B' != f[ly][lx]:
    lx += 1
rx = lx + 1
while rx < w and 'B' == f[ly][rx]:
    rx += 1
y = (ly + ry) // 2
x = (lx + rx) // 2
print(y + 1, x + 1)
